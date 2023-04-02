from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import login, register, edite_profile

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('edite_profile/', edite_profile, name='edite_profile'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout')
]
