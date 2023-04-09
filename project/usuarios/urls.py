from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import LoginView, RegisterView, UserEditView

urlpatterns = [
    path('login_view/', LoginView, name='login'),
    path('register/', RegisterView, name='register'),
    path('edite_profile/', UserEditView, name='edite_profile'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
]
