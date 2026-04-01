from django.urls import path
from app.views import CartaListCreate, CartaDetailChangeDelete
from . import views
urlpatterns = [
    path('', CartaListCreate.as_view()),
    path('<int:pk>/',CartaDetailChangeDelete.as_view()),
    path('grafico/<int:carta_id>/', views.CartaGraficoView.as_view())
]