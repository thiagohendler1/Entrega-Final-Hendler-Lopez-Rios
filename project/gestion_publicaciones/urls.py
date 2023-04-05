from django.urls import path
from gestion_publicaciones.views import HomeView, TiendaView, GenerosView, AboutView, PublicacionCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='inicio'),
    path('shop/', TiendaView, name='tienda'),
    path('shop/create_publication/', PublicacionCreateView.as_view(), name='crear_publicacion'),
    path('genres/', GenerosView, name='generos'),
    path('about/', AboutView.as_view(), name='sobre_nosotros'),
]