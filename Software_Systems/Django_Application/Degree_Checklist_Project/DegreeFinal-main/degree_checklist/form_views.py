from django.shortcuts import render, redirect
from .forms import (
    StudentForm, DegreeProgramForm, CourseForm, DegreeChecklistTemplateForm, StudentDegreeChecklistForm, CourseEnrollmentForm
)


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_records')
    else:
        form = StudentForm()
    return render(request, 'degree_checklist/forms/create_student.html', {'form': form})


def create_degree_program(request):
    if request.method == 'POST':
        form = DegreeProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_records')
    else:
        form = DegreeProgramForm()
    return render(request, 'degree_checklist/forms/create_degree_program.html', {'form': form})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_records')
    else:
        form = CourseForm()
    return render(request, 'degree_checklist/forms/create_course.html', {'form': form})


def create_degree_checklist_template(request):
    if request.method == 'POST':
        form = DegreeChecklistTemplateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_records')
    else:
        form = DegreeChecklistTemplateForm()
    return render(request, 'degree_checklist/forms/create_degree_checklist_template.html', {'form': form})


def create_student_degree_checklist(request):
    if request.method == 'POST':
        form = StudentDegreeChecklistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_records')
    else:
        form = StudentDegreeChecklistForm()
    return render(request, 'degree_checklist/forms/create_student_degree_checklist.html', {'form': form})


def create_course_enrollment(request):
    if request.method == 'POST':
        form = CourseEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_records')
    else:
        form = CourseEnrollmentForm()
    return render(request, 'degree_checklist/forms/create_course_enrollment.html', {'form': form})
