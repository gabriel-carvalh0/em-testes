"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from core import views
from django.views.generic.base import TemplateView

from django.contrib.auth.views import LoginView,  LogoutView


urlpatterns = [
    path('', LoginView.as_view(template_name="registration/login.html"), {'next_page':'home'}, name='entrar'),
    path('sair/', LogoutView.as_view(), {'next_page':'produtos'},  name='sair'),
    path('produtos/', TemplateView.as_view(template_name="produtos.html"), name="produtos"),
    path('registrar', views.register, name="register"),

    path('logado/', views.home, name="home"),
    path('logado/catalogo', views.product_list, name="catalogo"),
    path('logado/contato', views.contato, name="contato"),
    path('admin/', admin.site.urls),
]
