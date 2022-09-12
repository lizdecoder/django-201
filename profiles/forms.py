from django import forms
from .models import User, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class UpdateImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']