from rest_framework.decorators import api_view
from app.models import Carta
from app.serializers import CartaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import generics

class CartaListCreate(generics.ListCreateAPIView):
    queryset = Carta.objects.all()
    serializer_class = CartaSerializer
       
    
class CartaDetailChangeDelete(generics.RetrieveUpdateDestroyAPIView):
   queryset = Carta.objects.all()
   serializer_class = CartaSerializer