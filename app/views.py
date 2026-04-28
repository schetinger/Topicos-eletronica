from app.models import Media_Amplitude,imr,p,u
from app.serializers import CartaXr,CartaIMR,CartaP,CartaU
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from django.http import HttpResponse
from .utils import GerarRelatorioXr,GerarRelatorioIMR,GerarRelatorioU,GerarRelatorioP
from rest_framework.response import Response
from django.shortcuts import render



def pagina_inicial(request):
    # Isso vai renderizar o seu HTML de teste
    return render(request, 'front/index.html')

class CartaListCreate(generics.ListCreateAPIView):
    queryset = u.objects.all()
    serializer_class = CartaU
       
    
class CartaDetailChangeDelete(generics.RetrieveUpdateDestroyAPIView):
   queryset = u.objects.all()
   serializer_class = CartaU

class CartaGraficoMedia(APIView):
    def get(self, request,carta_id):
        try:
            carta = Media_Amplitude.objects.get(id=carta_id)
        except Media_Amplitude.DoesNotExist:
            return HttpResponse("carta nao encontrada", status=404)
        
        dados_brutos = carta
        buffer_imagem = grafico_media(dados_brutos)
        return HttpResponse(buffer_imagem.getvalue(),content_type="image/png")

class CartaGraficoAmplitude(APIView):
    def get(self, request,carta_id):
        try:
            carta = Media_Amplitude.objects.get(id=carta_id)
        except Media_Amplitude.DoesNotExist:
            return HttpResponse("carta nao encontrada", status=404)
        
        dados_brutos = carta
        buffer_imagem = grafico_amplitude(dados_brutos)
        return HttpResponse(buffer_imagem.getvalue(),content_type="image/png")

class CartaGraficoIMR(APIView):
        def get(self, request,carta_id):
            try:
                carta = imr.objects.get(id=carta_id)
            except imr.DoesNotExist:
                return HttpResponse("carta nao encontrada", status=404)
            
            dados_brutos = carta
            buffer_imagem = grafico_imr(dados_brutos)
            return HttpResponse(buffer_imagem.getvalue(),content_type="image/png")

class GeradorCEP(APIView):
    def post (self,request,*args, **kwargs):
        tipo_carta = request.data.get("chart")
        dados_medicao = request.data.get("measurements")

        if not tipo_carta or not dados_medicao:
            return Response(
                {"erro": "Você precisa enviar o tipo ('chart') e os dados ('measurements')."}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            if tipo_carta == "Xr":
                nova_carta = Media_Amplitude.objects.create(data=dados_medicao)
                return GerarRelatorioXr(nova_carta)

                
            elif tipo_carta == "IMR":
                nova_carta = imr.objects.create(data=dados_medicao)
                return GerarRelatorioIMR(nova_carta)
            
            elif tipo_carta =="u":
                nova_carta = u.objects.create(data=dados_medicao)
                return GerarRelatorioU(nova_carta)
            elif tipo_carta == "p":
                nova_carta = u.objects.create(data=dados_medicao)
                return GerarRelatorioP(nova_carta)
            else:
                return Response(
                    {"erro": f"O tipo de carta '{tipo_carta}' não é suportado."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(
                {
                    "mensagem": f"Carta {tipo_carta} gerada com sucesso!",
                    "id_carta": nova_carta.id,
                    "tipo de carta": tipo_carta,
                }, 
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                {"erro_interno": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    