from django.shortcuts import render, get_object_or_404
from vendas.models import *
from django.urls import reverse_lazy
from django.shortcuts import redirect

from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm  
from core.forms import ContactForm
from django.core.mail import send_mail


# Create your views here.



class HomeView(LoginRequiredMixin, TemplateView):
    model = User
    template_name = 'comeco.html'

    def boas_vindas(User):
        context = {
        'user' : User(),
        'categories': Category.objects()
        }
        return context()

home = HomeView.as_view()

def register(request):

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    context = {'form':form}
    
    return render(request, 'registrar.html', context)




# def contato(request):
#     success = False
#     form = ContactForm(request.POST or None)
#     if form.is_valid():
#         form.send_mail()
#         success = True
#     elif request.method == 'POST':
#         message.error(request, 'Formulário inválido')
#     context = {
#         'form': form,
#         'success': success
#     }
#     print(context)
#     return render(request, 'contato.html', context)

def contato(request):
    template_name = 'contato.html'
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            # message = 'Name : {0}E-Mail:{1}"{2}"'.format(name, email, message)
            send_mail(
                name,
                email,
                message,
                ['localhost'],
                fail_silently=False,
                )
        return redirect('home')

    context = {'form': form}
    return render(request, template_name, context)