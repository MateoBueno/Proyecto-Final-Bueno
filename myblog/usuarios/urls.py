from django.urls import path, include
from usuarios.views import registro, login_view, CustomLogoutView, ProfileUpdateView


urlpatterns = [
    path('registro/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('Editar-Perfil/', ProfileUpdateView.as_view(), name="editar_perfil")
]