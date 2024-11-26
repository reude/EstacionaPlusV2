from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro.html', views.cadastro, name='cadastro'),
]
