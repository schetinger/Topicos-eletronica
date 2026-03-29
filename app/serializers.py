from app.models import Carta
from rest_framework import serializers
class CartaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carta
        fields = ['id','media','dp','created_at']