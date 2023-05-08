import re
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django import forms

class User(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def clean(self):
        super().clean()

        if len(self.password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        if not re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', self.password):
            raise ValidationError(
                'Password must contain at least one uppercase letter, one lowercase letter, and one number.')


    def __str__(self):
        return self.username

class TextFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/')


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/')
    text = models.TextField()
    def __str__(self):
        return self.title

class Registration(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Articles(models.Model):
    create_date = models.DateTimeField(auto_now = True)
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name