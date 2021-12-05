from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('validado', views.revisao_validacao, name='validado')
]