from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views import generic

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

class CategoryListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'categorias.html'
    context_object_name = 'product_list'
    
    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

class CatalogListView(LoginRequiredMixin, generic.ListView):

    login_url = '/login/'
    template_name = 'catalogo.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.all()

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'produto.html', context)


category = CategoryListView.as_view()
catalog = CatalogListView.as_view()