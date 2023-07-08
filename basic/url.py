
from django.urls import path
from rest_framework import routers
from basic.views import ReservaModoViewset,reserva


app_name = 'reserva'

router = routers.SimpleRouter()
router.register('reservas',ReservaModoViewset,basename='reserva')

urlpatterns = [
path('reserve',reserva)
]

urlpatterns = urlpatterns + router.urls
print(type())