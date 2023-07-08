from rest_framework.serializers import ModelSerializer
from basic.models import ReservaModels

class ReservaSerialzer(ModelSerializer):

    class Meta:
        model = ReservaModels
        fields = '__all__'
                      



