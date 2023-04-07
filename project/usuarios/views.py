from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth. decorators import login_required
from usuarios.forms import *
from django.http import HttpResponse

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

def register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        print(form)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contra = form.cleaned_data['password1']
            user = authenticate(username=usuario, password=contra)
            form.save()

            if user is not None:
                login(user)
                mensaje = f"Bienvenido/a {request.POST['username']}"
                return render(request, 'gestion_publicaciones/inicio.html', {'mensaje':mensaje})

        else:
            return HttpResponse('Debes completar todos los campos para el registro...')

    else:
        form = UserRegisterForm()

    return render(request, 'usuarios/register.html', {'form':form})

def login_view(request):
    
#FALTA AGREGAR AL HTML las keys de los value. 
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            contra = form.cleaned_data['password']
            
            user = authenticate(username = usuario, password = contra)
            print(user)
            if user is not None:
                login(request, user)
                return render(request, 'gestion_publicaciones/inicio.html', {'mensaje': f"Bienvenido/a {usuario}"})
            
        else:
            return render(request, 'usuarios/login.html', {'mensaje': 'El usuario y la contraseña no coinciden', 'form': form})
    
    else:
        form = AuthenticationForm()
    
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

@login_required
def edite_profile(request):
    
    usuario = request.User
    
    if request.method == 'POST':
        myform = UserEditForm(request.POST)
        
        if myform.is_valid():
            
            information = myform.cleaned_data
            
            usuario.email = information['email']
            usuario.password1 = information['password1']
            usuario.password2 = information['password2']
            usuario.save()
            
            return render(request, 'inicio.html')
    else:
        myform = UserEditForm(initial={'email': usuario.email})
    
    return render(request, 'edit_profile.html', {'myform': myform, 'usuario': usuario})

