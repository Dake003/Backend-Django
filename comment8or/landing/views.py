from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import MyForm, Upd
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import RegisterUserForm, AuthUserForm

from django.forms import *

from .models import Cars, Image
from .forms import ImageForm



def submit_form(request):
	if request.method == 'POST':
		form = MyForm(request.POST)
		if form.is_valid():

			name = form.cleaned_data['name']
			password = form.cleaned_data['password']

			MyModel.objects.create(name=name, password=password)
			user = authenticate(name=name, password=password)
			login(request, user)
			return render(request, 'login.html')
	else:
		form = MyForm()
	return render(request, 'base.html', {'form': form})



def adm(request):
	context = {
		'list_cars': Cars.objects.all()
	}
	return render(request, 'adm1.html', context)

def tem(request):
	context = {
		'list_cars': Cars.objects.all()
	}
	return render(request, 'tem.html', context)


def update(request, pk):
	get_car = Cars.objects.get(pk=pk)
	if request.method == 'POST':
		form = Upd(request.POST, instance=get_car)
		if form.is_valid():
			form.save()
	context = {
		'get_car': get_car,
		'update': True,
		'form': Upd(instance=get_car)

	}
	return render(request, 'adm1.html', context)

def upload_image(request):
	get_car = Image.objects.get(id='1')
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		context = {
		'get_car': get_car,
		'upload': True,
		}
		return redirect('/success/', context)
	else:
		form = ImageForm()
	return render(request, 'upload.html', {'form': form})

def delete(request, pk):
	get_car = Cars.objects.get(pk=pk)
	get_car.delete()
	return redirect(reverse('submit_form'))



class MyLoginView(LoginView):
	template_name = 'login.html'
	form_class = AuthUserForm
	success_url = ('/success/')
	def get_success_url(self):
		return self.success_url



class Registrate(CreateView):
	model = User
	template_name = 'registration.html'
	form_class = RegisterUserForm
	success_url = ('/login/')
	success_msg = 'Пользователь создана'

def log1(request):
	return render(request, 'log1.html')