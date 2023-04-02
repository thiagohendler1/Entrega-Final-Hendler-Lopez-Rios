from django.shortcuts import render, redirect
# ------ Importaciones para el crud ------
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
# ----------------------------------------
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from gestion_publicaciones.models import Publicacion, Mensaje
from gestion_publicaciones.forms import NuevaPublicacionForm, EditarPublicacionForm, MensajeForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    model = Publicacion
    template_name = 'gestion_publicaciones/inicio.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Guardado de las publicaciones mas recientes
        objetos = Publicacion.objects.all().order_by('-id')[:3]
        objeto_uno = objetos[0]
        objeto_dos = objetos[1]
        objeto_tres = objetos[2]
        context.update({'objeto_uno': objeto_uno, 'objeto_dos': objeto_dos, 'objeto_tres': objeto_tres})
        return context