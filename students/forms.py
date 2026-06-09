from django import forms
from .models import Student

class StudentCreateForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )
    
    class Meta:
        model = Student
        
        fields = [
            'roll_number',
            'department',
            'year'
        ]