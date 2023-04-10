from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth. decorators import login_required
from usuarios.forms import *
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def register(request):
#     data = {
#         'form': CustomUserCreationForm()
#     }
    
#     if request.method == 'POST':
#         user_creation_form = CustomUserCreationForm(data=request.POST)
        
#         if user_creation_form.is_valid():
#             user_creation_form.save()
            
#             user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
#             login(request, user)
#             return redirect('inicio')
    
#     return render(request, 'usuarios/register.html', data)
#-----------------------------------------------------------------------------------------


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'usuarios/register.html', {'form': form})
#-----------------------------------------------------------------------------------------
# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
    
#     return render(request, 'usuarios/register.html', {'form': form})
#-----------------------------------------------------------------------------------------

# def register_view(request):

#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         print(form)
#         if form.is_valid():
#             usuario = form.cleaned_data['username']
#             contra = form.cleaned_data['password1']
#             user = authenticate(username=usuario, password=contra)
#             form.save()

#             if user is not None:
#                 login(user)
#                 mensaje = f"Bienvenido/a {request.POST['username']}"
#                 return render(request, 'gestion_publicaciones/inicio.html', {'mensaje':mensaje})

#         else:
#             return HttpResponse('Debes completar todos los campos para el registro...')

#     else:
#         form = UserRegisterForm()

#     return render(request, 'usuarios/register.html', {'form':form})


def RegisterView(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']
            contra = form.cleaned_data['password1']
            user = authenticate(username=usuario, password=contra)
            print(user)

            if user is not None:
                login(request, user)
                mensaje_user = f"{request.POST['first_name']}"
                return redirect('inicio')

        else:
            return HttpResponse('Debes completar todos los campos para el registro...')

    else:
        form = UserRegisterForm()

    return render(request, 'usuarios/register.html', {'form':form})


def LoginView(request):
    
#FALTA AGREGAR AL HTML las keys de los value. 
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contra = form.cleaned_data['password']
            
            user = authenticate(username = usuario, password = contra)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('inicio')
            
        else:
            return render(request, 'usuarios/login.html', {'mensaje': 'El usuario y la contraseña no coinciden', 'form': form})
    
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         print(request.POST)
#         usuario = request.POST['username']
#         contra = request.POST['password']
#         user = authenticate(request, username=usuario, password=contra)
#         if user is not None:
#             login(request, user)
#             return render(request, 'usuarios/inicio.html')
        
#         else:
#             return render(request, 'usuarios/login.html', {'mensaje': 'Credenciales inválidas.'})
        
#     else:
#         return render(request, 'usuarios/login.html')

# @login_required
# def edite_profile(request):
    
#     usuario = request.User
    
#     if request.method == 'POST':
#         myform = UserEditForm(request.POST)
        
#         if myform.is_valid():
            
#             information = myform.cleaned_data
            
#             usuario.email = information['email']
#             usuario.password1 = information['password1']
#             usuario.password2 = information['password2']
#             usuario.save()
            
#             return render(request, 'inicio.html')
#     else:
#         myform = UserEditForm(initial={'email': usuario.email})
    
#     return render(request, 'edit_profile.html', {'myform': myform, 'usuario': usuario})


@login_required
def UserEditView(request):
    usuario = request.user
    
    if request.method == 'POST':
        
        form1 = UserEditForm(request.POST)
        form2 = PasswordEditForm(request.user, request.POST)
        
        if 'submit1' in request.POST:
            if form1.is_valid():
                data = form1.cleaned_data
                usuario.email = data['email']
                usuario.first_name = data['first_name']
                usuario.last_name = data['last_name']
                usuario.username = data['username']
                usuario.save()
                
                return redirect('inicio')
            
        if 'submit2' in request.POST:
            if form2.is_valid():
                contra = form2.cleaned_data['new_password1']
                
                if contra:
                    usuario.set_password(contra)
                    usuario.save()
                    
                    return redirect('inicio')

    else:
        form1 = UserEditForm()
        form2 = PasswordEditForm(request.user)

    return render(request, 'usuarios/edit_profile.html', {'form1': form1, 'form2': form2})


@login_required
def AvatarView(request):
    
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        
        if form.is_valid():
            usuario = User.objects.get(username=request.user.username)
            imag = form.cleaned_data['imagen']
            
            existe_objeto = Avatar.objects.filter(user=usuario).exists()
            
            # Si el usuario ya tiene un avatar, lo actualiza
            if existe_objeto:
                avat = Avatar.objects.get(user=usuario)
                avat.imagen = imag
                avat.save()
                
            # Sino, lo agrega
            else:
                avat = Avatar(user=usuario, imagen=imag)
                avat.save()
            
            return redirect('inicio')
    
    else:
        form = AvatarForm()
    
    return render(request, 'usuarios/edit_avatar.html', {'form':form})