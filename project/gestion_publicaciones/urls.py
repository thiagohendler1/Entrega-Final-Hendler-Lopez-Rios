from django.urls import path
from gestion_publicaciones.views import HomeView, TiendaView, GenerosView, AboutView, PublicacionCreateView, PublicacionDetailView, PublicacionUpdateView, PublicacionDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='inicio'),
    path('shop/', TiendaView, name='tienda'),
    path('shop/create_publication/', PublicacionCreateView.as_view(), name='crear_publicacion'),
    path('shop/publication_detail/<int:pk>/', PublicacionDetailView.as_view(), name='detalle_publicacion'),
    path('shop/update_publication/<int:pk>/', PublicacionUpdateView.as_view(), name='editar_publicacion'),
    path('shop/<int:pk>/delete_publication/', PublicacionDeleteView, name='eliminar_publicacion'),
    path('genres/', GenerosView, name='generos'),
    path('about/', AboutView.as_view(), name='sobre_nosotros'),
]