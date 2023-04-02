from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import login_view, register, edite_profile

urlpatterns = [
    path('login_view/', login_view, name='login'),
    path('register/', register, name='register'),
    path('edite_profile/', edite_profile, name='edite_profile'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
]
