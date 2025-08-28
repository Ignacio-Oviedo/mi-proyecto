# C:\mi proyecto\core\views.py
from django.shortcuts import render

def home(request):
    # Esta vista renderizará tu archivo HTML de cosméticos
    return render(request, 'core/home.html', {'message': '¡Bienvenido a tu Tienda de Cosméticos!'})