from django import forms
from .models import Profile,Driver,Client
from django.contrib.auth.forms import AuthenticationForm


class ProfileForm(forms.ModelForm):
	model = Profile
	bio = forms.CharField(label='Image Caption',max_length=500)
	profile_pic = forms.ImageField(label = 'Image Field')
class DriverForm(forms.ModelForm):
	class Meta:
		model = Driver
		fields =['firstName', 'lastName', 'phone', 'plate_number']
class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['firstName', 'lastName', 'phone', 'packageId', 'driver']  
	

class ProfileUploadForm(forms.ModelForm):
	class Meta:
		model = Profile
		
		exclude = ['user']