from django.urls import path, include
from pagina_blog.views import (
  inicio,listar_noticias,publicar_noticias,
  buscar_noticias,ver_noticia, editar_noticia, eliminar_noticia,mi_info
)

urlpatterns = [
  path('Noticias/', listar_noticias, name='listar_noticias'),
  path('Publicar/', publicar_noticias, name= 'publicar_noticias'),
  path('Buscar/', buscar_noticias, name= 'buscar_noticias'),
  path('Ver/<int:id>', ver_noticia, name= 'ver_noticia'),
  path('Editar-Noticia/<int:id>', editar_noticia, name= 'editar_noticia'),
  path('Eliminar-noticia/<int:id>', eliminar_noticia, name='eliminar_noticia'),

  path('Acerca de mi/', mi_info, name='about')
]

