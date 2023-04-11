from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import LoginView, RegisterView, UserEditView, AvatarView

urlpatterns = [
    path('login_view/', LoginView, name='login'),
    path('register/', RegisterView, name='register'),
    path('edit_profile/', UserEditView, name='edit_profile'),
    path('edit_avatar/', AvatarView, name='edit_avatar'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
]
