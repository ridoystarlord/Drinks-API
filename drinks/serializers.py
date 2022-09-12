from rest_framework import routers, serializers, viewsets
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']
