from django.urls import path
from app.views import CartaListCreate, CartaDetailChangeDelete
from . import views
urlpatterns = [
    path('', CartaListCreate.as_view()),
    path('<int:pk>/',CartaDetailChangeDelete.as_view()),
    path('graficom/<int:carta_id>/', views.CartaGraficoMedia.as_view()),
    path('graficoa/<int:carta_id>/', views.CartaGraficoAmplitude.as_view())
]