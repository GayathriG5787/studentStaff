from django import forms
from .models import Student
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class StudentCreateForm(forms.ModelForm):
    username = forms.CharField()
    # used to hide the content when someone types in the password field
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
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        
        return password