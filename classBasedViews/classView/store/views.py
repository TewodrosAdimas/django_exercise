from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Products

# Create your views here.
class Prod(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Products.objects.all()
        return context