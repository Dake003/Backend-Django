from django.db import models
from django import forms

class MyModel(models.Model):
	name = models.CharField(max_length=100)
	password = models.CharField(max_length=100)


	def __str__(self):
		return self.name

class Cars(models.Model):
	objects = None
	name = models.CharField(max_length=100)

def __str__(self):
	return self.name




class Image(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/')