
from django.urls import re_path

urlpatterns = [
    re_path('carrinho/', corrinho.views, name="carrinho"),
]
