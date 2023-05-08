from django.contrib import messages
from django.core.mail import send_mail
from django.http import FileResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView

from .forms import LoginForm, RegistrationForm, AuthUserForm, RegisterUserForm,  TextFileForm, \
    RegistrationForms, LoginForms, ImageForm, UserForm
from django.contrib.auth.views import LoginView

from .models import Articles, Registration, TextFile, Image, User
from django.urls import reverse
from django.shortcuts import render, get_object_or_404


def show_image(request, id):
    obj = get_object_or_404(Image, pk=id)
    return render(request, 'base.html', {'obj': obj})

def base(request):
    return render(request, 'adminpanel.html')

def logins(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # redirect to home page after successful login
    else:
        form = LoginForms()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redirect to login page after successful registration
    else:
        form = RegistrationForms()
    return render(request, 'registration.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user = User(username=username, password=password, email=email)
            user.save()

            messages.success(request, 'Registration successful. Please log in.')
            return redirect('/login/')
    else:
        form = RegistrationForms()
    return render(request, 'registration.html', {'form': form})

def login(request):
    sx = False
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username, password=password)
                messages.success(request, 'Login successful. Welcome!')
                return redirect('/')  # Replace 'home' with the URL you want to redirect to after successful login
            except User.DoesNotExist:

                messages.error(request, 'Invalid username or password.')
                return render(request, 'login.html', {'form': form})
    else:
        form = LoginForms()
        sx =True

    return render(request, 'login.html', {'form': form})

def upload_text_file(request):
    if request.method == 'POST':
        form = TextFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/') # Replace "home" with the URL name of your homepage
    else:
        form = TextFileForm()
    return render(request, 'upload_text_file.html', {'form': form})


def view_text_file(request):
    with open('text_files/audi.jpg', 'rb') as f:
        response = FileResponse(f)
        response['Content-Type'] = 'text/plain'
        return response


def home(request):

    context = {
        'list_images': Image.objects.all(),

    }
    return render(request, 'base.html', context)

def detail(request,id):
    get_cars = Image.objects.get(id=id)
    context = {
        'get_cars': get_cars
    }
    return render(request, 'detail_page.html', context)

def profile(request):
    get_users = User.objects.latest('id')
    context = {
        'get_users': get_users
    }
    return render(request, 'profile.html', context)

def edit(request):
    success = False
    if request.method == 'POST':
        form = ImageForm(request.POST)
        forms = UserForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
    list_cars = Image.objects.all()
    list_profile = User.objects.all()
    list_c = TextFile.objects.all()
    context = {
        'list_cars':list_cars.order_by('id'),
        'form': ImageForm,
        'forms': UserForm,
        'success': success,
        'list_profile': list_profile,
        'list_c':list_c
    }
    return render(request, 'edit_page.html', context)

def update(request,pk):
    success_update = False
    get_image = Image.objects.get(pk=pk)
    get_user = Image.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImageForm(request.POST, instance=get_image)
        forms = UserForm(request.POST, instance=get_user)
        if form.is_valid():
            form.save()
            success_update = True
    context = {
        'get_image':get_image,
        'get_user': get_user,
        'update': True,
        'form': ImageForm(instance=get_image),
        'forms': UserForm(instance=get_user),
        'success_update':success_update
    }
    return render(request, 'edit_page.html', context)

def delete(request,pk):
    get_article = Articles.objects.get(pk=pk)
    get_article.delete()
    return redirect(reverse('edit_page'))