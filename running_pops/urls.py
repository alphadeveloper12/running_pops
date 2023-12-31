"""
URL configuration for running_pops project.

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
from django.urls import path, include
from web.views import *
from game.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('whitelist/', whitelist, name="whitelist"),
    path('submit_wallet/', submit_wallet, name="add-wallet"),
    path('about/', about, name="about"),
    path('action/', action, name="action"),
    path('tournament/', tournament, name="tournament"),
    path('benefits/', benefits, name="benefits"),
    path('benefits_form/', benefits_form, name="benefits_form"),
    path('season2/', unity_game, name='tournament'),
]
