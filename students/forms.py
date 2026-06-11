from django import forms
from .models import Student
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

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
            'roll_number',
            'department',
            'year'
        ]
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        User = get_user_model()
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username already taken.'
            )
            
        return username
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        
        try:
            validate_password(password)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)
        
        return password
    
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