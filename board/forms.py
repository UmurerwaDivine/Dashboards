from django import forms
from .models import Profile,Driver,Client
from django.contrib.auth.forms import AuthenticationForm


class ProfileForm(forms.ModelForm):
	model = Profile
	bio = forms.CharField(label='Image Caption',max_length=500)
	profile_pic = forms.ImageField(label = 'Image Field')
class DriverForm(forms.ModelForm):
	model = Driver
	exlude =['user']
class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['firstName', 'lastName', 'phone', 'packageId', 'driver']  
	

