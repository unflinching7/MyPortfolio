from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .models import Student, DegreeProgram, Course, DegreeChecklistTemplate, StudentDegreeChecklist, CourseEnrollment

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def clean_enrollment_year(self):
        enrollment_year = self.cleaned_data.get('EnrollmentYear')

        # validation logic
        if enrollment_year < 2000:
            raise forms.ValidationError("Enrollment year must be after 2000.")

        return enrollment_year

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Row(
                Column('Name', css_class='col-md-6'),
                Column('ContactInfo', css_class='col-md-6'),
            ),
            Row(
                Column('EnrollmentYear', css_class='col-md-6'),
            ),
            Submit('submit', 'Submit', css_class='btn btn-primary'),
        )

class DegreeProgramForm(forms.ModelForm):
    class Meta:
        model = DegreeProgram
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        # Add layout for DegreeProgramForm if needed

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        # Add layout for CourseForm if needed

class DegreeChecklistTemplateForm(forms.ModelForm):
    class Meta:
        model = DegreeChecklistTemplate
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        # Add layout for DegreeChecklistTemplateForm if needed

class StudentDegreeChecklistForm(forms.ModelForm):
    class Meta:
        model = StudentDegreeChecklist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        # Add layout for StudentDegreeChecklistForm if needed

class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = CourseEnrollment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        # Add layout for CourseEnrollmentForm if needed

class DataImportForm(forms.Form):
    data_file = forms.FileField(label="Select a data file for import")
