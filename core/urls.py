# C:\mi proyecto\core\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # La URL raíz de la app 'core'
]