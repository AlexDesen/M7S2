
from rest_framework.viewsets import ModelViewSet
from basic.models import ReservaModels
from basic.serializer import ReservaSerialzer


""" 
   Url: http://127.0.0.1:8000/reserva/reservas/
   O serviços fornecido pela url esta relacionado ao resgate, envio, exclusão e 
   auteração de dados no nosso banco. """


class ReservaModoViewset(ModelViewSet):
   
   queryset = ReservaModels.objects.all() 
   serializer_class = ReservaSerialzer
   
  







   