from django import forms


from app.models import *
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields='__all__'


        