from django.shortcuts import render, get_object_or_404
from core.models import *
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm  
from core.forms import ContactForm


# Create your views here.



class HomeView(LoginRequiredMixin, TemplateView):
    
    template_name = 'comeco.html'



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





class CatalogListView(LoginRequiredMixin, generic.ListView):

    login_url = '/login/'
    template_name = 'produtos.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()



def contato(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    elif request.method == 'POST':
        message.error(request, 'Formulário inválido')
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contato.html', context)

product_list = CatalogListView.as_view()