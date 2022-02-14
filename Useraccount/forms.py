from django import forms
from .models import Accounts


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = '__all__'
        widgets = {
            'profile_image': forms.ImageField(attrs={'class': ''}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'True', 'autocomplete': "off"})
        }
        labels = {
            'profile_image': 'Upload your profile picture',
            'name': 'Student Name:',
            'phone_number': 'Student Mobile Number:',
            'email': 'Student Email:',
            'password': 'Set Password:',
            'confirm_password': 'Confirm Password:',
        }