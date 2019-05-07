from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
	profile_pic = models.ImageField(upload_to = "profile/",null=True)
	bio = models.TextField(default='',blank = True)
	user=models.ForeignKey(User,null=True)

	def __str__(self):
		return self.username

	def delete_profile(self):
		self.delete()

	def save_profile(self):
		self.save()
class Driver(models.Model):
	firstName = models.CharField(default='',max_length=60)
	lastName = models.CharField(default='',max_length=60)
	phone = models.CharField(default='',max_length=60)
	plate_number = models.CharField(default='',max_length=30)
	pub_date = models.DateTimeField(auto_now_add=True,null=True)
	user=models.ForeignKey(User,null=True)

class Client(models.Model):
	firstName = models.CharField(default='',max_length=60)
	lastName = models.CharField(default='',max_length=60)
	phone = models.CharField(default='',max_length=60)
	packageId = models.CharField(default='',max_length=10)
	driver = models.ForeignKey(Driver,null=True)
	user=models.ForeignKey(User,null=True)



