from django.urls import path, include
from django.views.generic import TemplateView
from .views import Prod

urlpatterns = [
    path("home/", TemplateView.as_view(template_name = "home.html", extra_context = {'name': 'First TemplateView'})),
    path("products/",Prod.as_view()), #template view

]