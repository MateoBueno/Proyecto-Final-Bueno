from django.urls import path, include
from pagina_blog.views import inicio,listar_noticias,publicar_noticias,buscar_noticias

urlpatterns = [
  path('Noticias/', listar_noticias, name='listar_noticias'),
  path('Publicar/', publicar_noticias, name= 'publicar_noticias'),
  path('Buscar/', buscar_noticias, name= 'buscar_noticias'),
]

