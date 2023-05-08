"""
URL configuration for assainment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static

from tengri import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='main'),
    path('edit/', views.edit, name='edit_page'),
    path('update/<int:pk>', views.update, name='update_page'),
    path('delete/<int:pk>', views.delete, name='delete_page'),
    path('detail/<int:id>', views.detail, name='detail_page'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login_page'),
    path('reg/', views.register, name='register_page'),
    path('upload/', views.upload_text_file, name='upload_text_file'),
    path('uploa/', views.view_text_file, name='view_text_file'),
    path('profile/', views.profile, name='profile'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
