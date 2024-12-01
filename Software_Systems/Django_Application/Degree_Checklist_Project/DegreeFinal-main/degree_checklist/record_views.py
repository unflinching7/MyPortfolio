from django.views.generic import ListView
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment


class StudentAllRecordsView(ListView):
    model = Student
    template_name = 'degree_checklist/student_records.html'
    context_object_name = 'student_records'

    def get_queryset(self):
        sort_by = self.request.GET.get(
            'sort_by', 'Name')  # Default sort by Name
        return self.model.objects.all().order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort_by')
        return context


class DegreeProgramAllRecordsView(ListView):
    model = DegreeProgram
    template_name = 'degree_checklist/degree_program_records.html'
    context_object_name = 'degree_program_records'

    def get_queryset(self):
        # Default sort by ProgramName
        sort_by = self.request.GET.get('sort_by', 'ProgramName')
        return self.model.objects.all().order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort_by')
        return context


class CourseAllRecordsView(ListView):
    model = Course
    template_name = 'degree_checklist/course_records.html'
    context_object_name = 'course_records'

    def get_queryset(self):
        # Default sort by CourseName
        sort_by = self.request.GET.get('sort_by', 'CourseName')
        return self.model.objects.all().order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort_by')
        return context


class DegreeChecklistTemplateAllRecordsView(ListView):
    model = DegreeChecklistTemplate
    template_name = 'degree_checklist/degree_checklist_template_records.html'
    context_object_name = 'checklist_template_records'

    def get_queryset(self):
        # Default sort by TemplateName
        sort_by = self.request.GET.get('sort_by', 'TemplateName')
        return self.model.objects.all().order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort_by')
        return context


class StudentDegreeChecklistAllRecordsView(ListView):
    model = StudentDegreeChecklist
    template_name = 'degree_checklist/student_degree_checklist_records.html'
    context_object_name = 'student_degree_checklist_records'

    def get_queryset(self):
        # Default sort by ChecklistName
        sort_by = self.request.GET.get('sort_by', 'ChecklistName')
        return self.model.objects.all().order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort_by')
        return context


class CourseEnrollmentAllRecordsView(ListView):
    model = CourseEnrollment
    template_name = 'degree_checklist/course_enrollment_records.html'
    context_object_name = 'course_enrollment_records'

    def get_queryset(self):
        # Default sort by EnrollmentID
        sort_by = self.request.GET.get('sort_by', 'EnrollmentID')
        return self.model.objects.all().order_by(sort_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_by'] = self.request.GET.get('sort_by')
        return context
