from django.urls import path, include
from django.conf.urls import url
from vendas import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^categorias/(?P<slug>.*)/$', views.category, name="category"),
    url('catalogo/', views.catalog, name="catalogo"),
    url(r'^produtos/(?P<slug>.*)/$', views.product, name='produto'),
]