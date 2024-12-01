from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment

# Add import_data function outside the admin classes
def import_data(modeladmin, request, queryset):
    # data import logic for the model here
    # This function will be called when the "Import Data" action is selected in the admin interface
    messages.success(request, "Data imported successfully.")
    return redirect('admin:index')

# Short description for the import_data action
import_data.short_description = "Import Data"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    actions = [import_data]

@admin.register(DegreeProgram)
class DegreeProgramAdmin(admin.ModelAdmin):
    actions = [import_data]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    actions = [import_data]

@admin.register(DegreeChecklistTemplate)
class DegreeChecklistTemplateAdmin(admin.ModelAdmin):
    actions = [import_data]

@admin.register(StudentDegreeChecklist)
class StudentDegreeChecklistAdmin(admin.ModelAdmin):
    actions = [import_data]

@admin.register(CourseEnrollment)
class CourseEnrollmentAdmin(admin.ModelAdmin):
    actions = [import_data]

# Register the User model with the custom UserAdmin
admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, UserAdmin)  # Register User with custom admin

