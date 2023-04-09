from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import login_view, register_view, UserEditView

urlpatterns = [
    path('login_view/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('edite_profile/', UserEditView, name='edite_profile'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
]
