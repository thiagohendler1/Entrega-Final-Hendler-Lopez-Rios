from django.urls import path
from gestion_publicaciones.views import HomeView, TiendaView, GenerosView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='inicio'),
    path('shop/', TiendaView, name='tienda'),
    path('genres/', GenerosView, name='generos'),
    path('about/', AboutView.as_view(), name='sobre_nosotros'),
]