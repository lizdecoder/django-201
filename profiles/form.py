from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UpdateUserForm(forms.ModelForm):
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)
	username = forms.CharField(max_length=100)
	
	class Meta: 
		model = User
		fields = ['first_name', 'last_name', 'username']

class UpdateProfileForm(forms.ModelForm):
	image = forms.FileField()

	class Meta:
		model = Profile
		fields = ['image']
