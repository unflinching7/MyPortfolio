from django.db import models

# Define the Student model


class Student(models.Model):
    StudentID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    ContactInfo = models.CharField(max_length=255)
    EnrollmentYear = models.IntegerField()

    def __str__(self):
        return self.Name

# Define the DegreeProgram model


class DegreeProgram(models.Model):
    ProgramID = models.AutoField(primary_key=True)
    ProgramName = models.CharField(max_length=100)
    ProgramCode = models.CharField(max_length=20)
    TotalCredits = models.IntegerField()

    def __str__(self):
        return self.ProgramName

# Define the Course model


class Course(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CourseName = models.CharField(max_length=100)
    CourseCode = models.CharField(max_length=20)
    CreditHours = models.IntegerField()

    def __str__(self):
        return self.CourseName

# Define the DegreeChecklistTemplate model


class DegreeChecklistTemplate(models.Model):
    TemplateID = models.AutoField(primary_key=True)
    TemplateName = models.CharField(max_length=100)
    AcademicYear = models.CharField(max_length=20)
    DegreeProgram = models.ForeignKey(DegreeProgram, on_delete=models.CASCADE)

    def __str__(self):
        return self.TemplateName

# Define the StudentDegreeChecklist model


class StudentDegreeChecklist(models.Model):
    ChecklistID = models.AutoField(primary_key=True)
    ChecklistName = models.CharField(max_length=100)

    STATUS_CHOICES = (
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('inactive', 'Inactive'),
        # Add more choices as needed
    )

    Status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='active')

    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Template = models.ForeignKey(
        DegreeChecklistTemplate, on_delete=models.CASCADE)

    def __str__(self):
        return self.ChecklistName


# Define the CourseEnrollment model


class CourseEnrollment(models.Model):
    ENROLLMENT_CHOICES = (
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
        # Add more choices as needed
    )

    EnrollmentID = models.AutoField(primary_key=True)
    EnrollmentStatus = models.CharField(
        max_length=20, choices=ENROLLMENT_CHOICES, default='enrolled')
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Student} - {self.Course}"
