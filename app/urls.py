from django.urls import path
from app.views import pagina_inicial
from . import views
urlpatterns = [
    path('',pagina_inicial, name='home'),
    #path('<int:pk>/',CartaDetailChangeDelete.as_view()),
    #path('graficom/<int:carta_id>/', views.CartaGraficoMedia.as_view()),
    #path('graficoa/<int:carta_id>/', views.CartaGraficoAmplitude.as_view()),
    #path('graficoimr/<int:carta_id>/',views.CartaGraficoIMR.as_view()),
    path('gerar-carta/',views.GeradorCEP.as_view())

]