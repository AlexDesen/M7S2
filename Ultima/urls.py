

from django.contrib import admin
from django.urls import path, include
from basic.views import inicio
from basic.views import modelo
from basic.views import reserva
from reservando.views import criar_reserva
from eventos.views import eventos



urlpatterns = [    
    path('reserva/',include('basic.url',namespace='reservas')),
    path("admin/", admin.site.urls),
    path('api_auth/',include('rest_framework.urls')),   
    ]
