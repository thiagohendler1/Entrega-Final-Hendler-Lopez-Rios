from django.urls import path
from gestion_publicaciones.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='inicio'),
]