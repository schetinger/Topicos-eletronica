from app.models import Media_Amplitude
from app.serializers import CartaSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django.http import HttpResponse
from .utils import gerar_grafico_da_carta,grafico_individual

class CartaListCreate(generics.ListCreateAPIView):
    queryset = Media_Amplitude.objects.all()
    serializer_class = CartaSerializer
       
    
class CartaDetailChangeDelete(generics.RetrieveUpdateDestroyAPIView):
   queryset = Media_Amplitude.objects.all()
   serializer_class = CartaSerializer

class CartaGraficoView(APIView):
    def get(self, request,carta_id):
        try:
            carta = Media_Amplitude.objects.get(id=carta_id)
        except Media_Amplitude.DoesNotExist:
            return HttpResponse("carta nao encontrada", status=404)
        
        dados_brutos = carta
        buffer_imagem = grafico_individual(dados_brutos)
        return HttpResponse(buffer_imagem.getvalue(),content_type="image/png")