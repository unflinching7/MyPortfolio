from django import template

register = template.Library()

@register.filter(name='uppercase')
def uppercase(value):
    return value.upper()
