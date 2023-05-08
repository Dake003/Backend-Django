
from django.shortcuts import render, redirect
from .forms import MyForm, Upd
from .models import MyModel, Cars, Image
from django.urls import reverse

def success(request):
	context = {
		'cars': Cars.objects.get(id='1'),
		'cars1': Cars.objects.get(id='2'),
		'cars2': Cars.objects.get(id='3'),
		'cars3': Cars.objects.get(id='4'),
		'get_car': Image.objects.all(),
		'upload': True,
	}
	return render(request, 'success.html', context)