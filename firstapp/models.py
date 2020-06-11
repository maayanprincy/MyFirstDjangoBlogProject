from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class team(models.Model):
	firstname=models.CharField(max_length=100)
	lastname=models.CharField(max_length=100)
	desc=models.TextField()
	date_added=models.DateTimeField(default=timezone.now)
	username=models.ForeignKey(User,on_delete=models.CASCADE)
# Create your models here.
	def __str__(self):
		return self.firstname
		


class blog(models.Model):
	title=models.CharField(max_length=100)
	content=models.TextField()
	date_added=models.DateTimeField(default=timezone.now)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
# Create your models here.
	def __str__(self):
		return self.title
		
	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})