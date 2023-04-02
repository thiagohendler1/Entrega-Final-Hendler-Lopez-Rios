from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth. decorators import login_required
from usuarios.forms import *

# Create your views here.

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        
        if user_creation_form.is_valid():
            user_creation_form.save()
            
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('inicio')
    
    return render(request, 'usuarios/register.html', data)


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'usuarios/register.html', {'form': form})

def login(request):
    
#FALTA AGREGAR AL HTML las keys de los value. 
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username = usuario, password = contra)
            
            if user is not None:
                login(request, user)
                return render(request, 'inicio.html', {'mensaje': f"Bienvenido/a {usuario}"})
            
            else:
                return render(request, 'inicio.html', {'mensaje': 'Error en los datos.'})
            
        else: 
            return render(request, 'incio.html', {'mensaje': 'Formulario erroneo'})
    
    form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def logout(request):
    pass

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
