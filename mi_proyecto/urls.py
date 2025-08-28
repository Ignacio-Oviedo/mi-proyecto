# C:\mi proyecto\mi_proyecto\urls.py
from django.contrib import admin
from django.urls import path, include # Asegúrate de que 'include' esté aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), # ¡Esta línea enlaza las URLs de tu app 'core'!
]