# degree_checklist/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment
from .views import all_records, StudentAllRecordsView, DegreeProgramAllRecordsView, CourseAllRecordsView, DegreeChecklistTemplateAllRecordsView, StudentDegreeChecklistAllRecordsView, CourseEnrollmentAllRecordsView

class ModelTests(TestCase):
    def test_str_representation(self):
        # Test __str__ representation for each model
        student = Student(Name="John Doe", ContactInfo="john@example.com", EnrollmentYear=2022)
        self.assertEqual(str(student), "John Doe")

        degree_program = DegreeProgram(ProgramName="Computer Science", ProgramCode="CS", TotalCredits=120)
        self.assertEqual(str(degree_program), "Computer Science")

        course = Course(CourseName="Introduction to Programming", CourseCode="CS101", CreditHours=3)
        self.assertEqual(str(course), "Introduction to Programming")

        degree_program = DegreeProgram(ProgramName="Computer Science", ProgramCode="CS", TotalCredits=120)
        checklist_template = DegreeChecklistTemplate(TemplateName="CS Degree Checklist", AcademicYear="2022", DegreeProgram=degree_program)
        self.assertEqual(str(checklist_template), "CS Degree Checklist")

        student = Student(Name="John Doe", ContactInfo="john@example.com", EnrollmentYear=2022)
        degree_program = DegreeProgram(ProgramName="Computer Science", ProgramCode="CS", TotalCredits=120)
        checklist_template = DegreeChecklistTemplate(TemplateName="CS Degree Checklist", AcademicYear="2022", DegreeProgram=degree_program)
        student_degree_checklist = StudentDegreeChecklist(ChecklistName="John's Checklist", Status="active", Student=student, Template=checklist_template)
        self.assertEqual(str(student_degree_checklist), "John's Checklist")

        student = Student(Name="John Doe", ContactInfo="john@example.com", EnrollmentYear=2022)
        course = Course(CourseName="Introduction to Programming", CourseCode="CS101", CreditHours=3)
        enrollment = CourseEnrollment(EnrollmentStatus="enrolled", Student=student, Course=course)
        self.assertEqual(str(enrollment), "John Doe - Introduction to Programming")

class ViewTests(TestCase):
    def setUp(self):
        # Create test data for views
        Student.objects.create(Name="John Doe", ContactInfo="john@example.com", EnrollmentYear=2022)
        DegreeProgram.objects.create(ProgramName="Computer Science", ProgramCode="CS", TotalCredits=120)
        Course.objects.create(CourseName="Introduction to Programming", CourseCode="CS101", CreditHours=3)
        DegreeChecklistTemplate.objects.create(TemplateName="CS Degree Checklist", AcademicYear="2022", DegreeProgram_id=1)
        StudentDegreeChecklist.objects.create(ChecklistName="John's Checklist", Status="active", Student_id=1, Template_id=1)
        CourseEnrollment.objects.create(EnrollmentStatus="enrolled", Student_id=1, Course_id=1)

    def test_all_records_view(self):
        url = reverse('all_records')  # Assuming 'all_records' is the name in your urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertTemplateUsed(response, 'degree_checklist/all_records.html')

    def test_student_records_view(self):
        url = reverse('student_records')  # Assuming 'student_records' is the name in your urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertTemplateUsed(response, 'degree_checklist/student_records.html')

  

