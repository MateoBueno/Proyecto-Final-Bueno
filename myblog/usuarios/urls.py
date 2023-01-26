from django.urls import path, include
from usuarios.views import registro


urlpatterns = [
    path('registro/', registro, name="registro")
]