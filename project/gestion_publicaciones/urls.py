from django.urls import path
from gestion_publicaciones.views import HomeView, TiendaView

urlpatterns = [
    path('', HomeView.as_view(), name='inicio'),
    path('shop/', TiendaView, name='tienda'),
]