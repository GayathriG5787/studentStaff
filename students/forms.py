from django import forms
from .models import Student
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
import re

class StudentCreateForm(forms.ModelForm):
    username = forms.CharField()
    # used to hide the content when someone types in the password field
    password = forms.CharField(
        widget=forms.PasswordInput
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
    )
    
    # To tell which model to use and which fields to include
    class Meta:
        model = Student
        
        fields = [
            'name',
            'roll_number',
            'department',
            'year'
        ]
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        # Minimum length
        if len(username) < 3:
            raise forms.ValidationError(
                "Username must contain atleast 3 characters."
            )
            
        # Maximum length
        if len(username) > 50:
            raise forms.ValidationError(
                'Username cannot exceed 50 characters'
            )
        
        
        # Only letters and numbers allowed
        # fullmatch() checks whether the entire string matches the pattern
        # r here means raw string
        if not re.fullmatch(r'[A-Za-z0-9]+', username):
            raise forms.ValidationError(
                'Username can contain only letters and numbers.'
            )
            
        # Cannot be only numbers
        if username.isdigit():
            raise forms.ValidationError(
                'Username cannot contain only numbers.'
            )
        
        User = get_user_model()
        
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError(
                'Username already taken.'
            )
            
        return username
    
    def clean_name(self):
        name = self.cleaned_data.get('name').strip()
        
        if len(name) < 3:
            raise forms.ValidationError(
                'Student name must contain at least 3 characters'
            )
            
        if len(name) > 50:
            raise forms.ValidationError(
                'Student name cannot exceed 50 characters'
            )
            
        if not re.fullmatch(r'[A-Za-z ]+', name):
            raise forms.ValidationError(
                'Student name can contain only letters and spaces.'
            )
            
        return name
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        
        return password
    
    def clean_roll_number(self):
        roll_number = self.cleaned_data.get('roll_number')
        
        if not roll_number.isdigit():
            raise forms.ValidationError(
                'Roll number can contain only numbers'
            )
            
        return roll_number
    
    def clean(self):
        cleaned_data = super().clean()
        
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password:
            if password != confirm_password:
                self.add_error(
                    'confirm_password',
                    'Passwords do no match.'
                )
                
        return cleaned_data