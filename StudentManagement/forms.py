from django import forms
from .models import Student, RegistrationID

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        #fields =['firstName', 'lastName', 'semester', 'phoneNumber', 'age', 'gender']

        '''
        You Can use any of them.
        
        fields = '__all__'
        fields =['firstName', 'lastName', 'semester', 'phoneNumber', 'age', 'gender']
        '''
class RegistrationIDForm(forms.ModelForm):
    class Meta:
        model = RegistrationID
        fields = '__all__'
        #fields =('studentID', 'studentRoll', 'Student_RegistrationID')