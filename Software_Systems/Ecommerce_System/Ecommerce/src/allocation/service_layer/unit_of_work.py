from __future__ import annotations
import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from allocation import config
from allocation.adapters import repository


class AbstractUnitOfWork(abc.ABC):
    service_offerings: repository.AbstractRepository

    def __enter__(self) -> AbstractUnitOfWork:
    return self


def __exit__(self, *args):
    self.rollback()


def commit(self):
    self._commit()


def collect_new_events(self):
    for service_offering in self.service_offerings.seen:
        while service_offering.events:
            yield service_offering.events.pop(0)


@abc.abstractmethod
def _commit(self):
    raise NotImplementedError


@abc.abstractmethod
def rollback(self):
    raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        # substituting POSTGRES with the in-memory sqlite
        # config.get_postgres_uri(),
        "sqlite+pysqlite:///:memory:",
        echo=True,
        config.get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.service_offerings = repository.SqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
