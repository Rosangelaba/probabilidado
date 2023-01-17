from django.urls import path, re_path, include, register_converter

from django.views.generic import TemplateView

from . import views

app_name = 'probdado'

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
]
