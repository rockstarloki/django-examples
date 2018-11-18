"""project13 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from app13 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showLogin),
    path('register/', views.showRegister),
    path('login/', views.showLogin),
    path('savedetails/', views.saveDetails),
    path('logincheck/', views.loginCheck),
    path('logincheck/', views.loginCheck),
    path('view/', views.view),
    path('updateprofile/', views.updateProfile),
    path('updatedetails/', views.updateDetails),
    path('deleteprofile/', views.deleteProfile),
    path('deleteproduct/', views.deleteproduct),
    path('logout/', views.logOut),
]
