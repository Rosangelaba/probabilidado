from django.urls import path, re_path, include, register_converter

from django.views.generic import TemplateView

from . import views

app_name = 'probdado'

urlpatterns = [
    #~ path('', views.Main.as_view(), name='main'),
    path('rodada/<int:pk>/', views.View_Rodada.as_view(), name='rodada'),
    path('revelar/<int:rodada_pk>/', views.View_Revelar.as_view(), name='revelar'),
    path('novarodada/<int:match_pk>/', views.View_NovaRodada.as_view(), name='novarodada'),
    path('novacombinacao/<int:room_pk>/', views.View_NovaCombinacao.as_view(), name='novacombinacao'),
]
