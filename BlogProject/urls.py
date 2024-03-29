"""BlogProject URL Configuration

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
from django.urls import path , include 
from blog.views import home_view , about_view , contact_view , loginuser , register , logoutuser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', home_view , name='homepage'),
    path('about/', about_view , name='aboutpage'),
    path('contact/', contact_view , name='contactpage'),
    path('loginuser/', loginuser , name='loginuser'),
    path('logoutuser/', logoutuser , name='logoutuser'),
    path('register', register , name='register'),
]
