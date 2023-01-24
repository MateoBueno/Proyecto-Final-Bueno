from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from pagina_blog.models import Noticias
from pagina_blog.forms import NoticiaFormulario



def inicio(request):
    return render(
        request=request,
        template_name='pagina_blog/base.html'
        )

def listar_noticias(request):
    contexto = {
        'noticias' : Noticias.objects.all()
    }
    return render(
        request = request,
        template_name = 'pagina_blog/lista_noticias.html',
        context = contexto
    ) 

def publicar_noticias(request):
    if request.method == "POST":
         formulario = NoticiaFormulario(request.POST)

         if formulario.is_valid():
             data = formulario.cleaned_data
             noticia = Noticias(
                 titulo=data['titulo'], 
                 subtitulo=data['subtitulo'], 
                 fecha_publicacion=data['fecha_publicacion'], 
                 autor=data['autor']
                 )
             noticia.save()
             url_exitosa = reverse('listar_noticias')
             return redirect(url_exitosa)
    else: 
         formulario = NoticiaFormulario()
    return render(
         request=request,
         template_name='pagina_blog/form_noticias.html',
         context={'formulario': formulario},
    )

# class NoticiaCreateView(CreateView):
#     model = Noticias
#     fields = ['titulo','subtitulo','fecha_publicacion','autor']
#     success_url = reverse_lazy('listar_noticas')
#     template_name = 'pagina_blog/form_noticias.html'