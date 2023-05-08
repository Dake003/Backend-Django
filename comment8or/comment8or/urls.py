"""comment8or URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin


from django.urls import path
from django.urls import path

from landing.success import success
from landing import views

urlpatterns = [
    path('sb/', views.submit_form, name='submit_form'),
	path('success/', success, name='success'),
    path('adm/', views.adm, name='adm'),
    path('update/<int:pk>', views.update, name='upd'),
    path('del/<int:pk>', views.delete, name='del'),
    path('logins/', views.login, name='logins'),
    path('tem/', views.tem, name='tem'),
    path('register/', views.Registrate.as_view(), name='register_page'),
    path('login/', views.MyLoginView.as_view(), name='login_page'),
    path('admin/', admin.site.urls),
    path('upload/', views.upload_image, name='upload_image'),
    path('log1/', views.log1, name='image'),

]
