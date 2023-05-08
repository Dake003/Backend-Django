from django import forms
from .models import MyModel, Cars
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']

class MyForm(forms.ModelForm):
	class Meta:
		model = MyModel
		fields = ['name', 'password']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control'}),
		}

class Upd(forms.ModelForm):
	class Meta:
		model = Cars
		fields = ['name']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'})

		}


class RegisterUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
	def save(self, commit=True):
		user = super().save(commit = False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user

class AuthUserForm(AuthenticationForm, forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'