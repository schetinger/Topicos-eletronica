from django.urls import path
from app.views import CartaListCreate, CartaDetailChangeDelete
urlpatterns = [
    path('', CartaListCreate.as_view()),
    path('<int:pk>/',CartaDetailChangeDelete.as_view())
]