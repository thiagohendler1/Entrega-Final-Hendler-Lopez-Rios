from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# ------ Importaciones para el crud ------
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.views.decorators.http import require_http_methods
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
        if objetos:
            objeto_uno = objetos[0] if len(objetos) >= 1 else None
            objeto_dos = objetos[1] if len(objetos) >= 2 else None
            objeto_tres = objetos[2] if len(objetos) >= 3 else None
            context.update({'objeto_uno': objeto_uno, 'objeto_dos': objeto_dos, 'objeto_tres': objeto_tres, 'objetos': objetos})
        return context

# LOGIN REQUIRED
def TiendaView(request):
    object_list = Publicacion.objects.all()
    
    # No API-Form
    if request.method == 'POST':
        if 'filter_form' in request.POST:
            if request.POST['filter_select'] != 'noselect':
                seleccion = request.POST['filter_select']
                object_list = Publicacion.objects.filter(genero_libro=seleccion)
                mensaje = f'Haz filtrado por {seleccion}'
                
                return render(request, 'gestion_publicaciones/tienda.html', {'object_list': object_list, 'mensaje': mensaje})
            
            else:
                object_list = Publicacion.objects.all()
                return render(request, 'gestion_publicaciones/tienda.html', {'object_list': object_list})
        
        elif 'search_form' in request.POST:
            if request.POST['searched_product'] == '' or request.POST['searched_product'].isspace():
                object_list = Publicacion.objects.all()
                return render(request, 'gestion_publicaciones/tienda.html', {'object_list': object_list})
            
            else:
                object_list = Publicacion.objects.filter(titulo_libro__icontains=request.POST['searched_product'].strip())
                mensaje = f'Haz buscado "{request.POST["searched_product"]}"'
                return render(request, 'gestion_publicaciones/tienda.html', {'object_list': object_list, 'mensaje': mensaje})
    
    # Si request.method = GET, entonces el usuario vino por localhost:xxxx/genres/ 
    else:
        if request.GET:
            categoria = request.GET['filter_select']
            object_list = Publicacion.objects.filter(genero_libro=categoria)
            
            return render(request, 'gestion_publicaciones/tienda.html', {'object_list': object_list})
        
    return render(request, 'gestion_publicaciones/tienda.html', {'object_list': object_list})


# LOGIN REQUIRED
def GenerosView(request):
    return render(request, 'gestion_publicaciones/generos.html')


class AboutView(TemplateView):
    template_name = 'gestion_publicaciones/about.html'


# -------- CRUD de publicaciones --------


class PublicacionCreateView(LoginRequiredMixin, CreateView):
    model = Publicacion
    template_name = 'gestion_publicaciones/crear_publicacion.html'
    form_class = NuevaPublicacionForm
    success_url = reverse_lazy('inicio')
    
    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super(PublicacionCreateView, self).form_valid(form)
    
    
class PublicacionDetailView(LoginRequiredMixin, DetailView):
    model = Publicacion
    template_name = 'gestion_publicaciones/detalle_publicacion.html'


class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Publicacion
    template_name = 'gestion_publicaciones/editar_publicacion.html'
    success_url = reverse_lazy('tienda')
    form_class = EditarPublicacionForm
    

@require_http_methods(['DELETE'])
def PublicacionDeleteView(request, pk):
    publi = get_object_or_404(Publicacion, pk=pk)
    publi.delete()
    return HttpResponse(status=204)