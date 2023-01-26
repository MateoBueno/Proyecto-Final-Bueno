from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from pagina_blog.models import Noticias
from pagina_blog.forms import NoticiaFormulario



def inicio(request):
    return render(
        request=request,
        template_name='pagina_blog/inicio.html'
        )

@login_required
def listar_noticias(request):
    contexto = {
        'noticias' : Noticias.objects.all()
    }
    return render(
        request = request,
        template_name = 'pagina_blog/lista_noticias.html',
        context = contexto
    ) 

@login_required
def publicar_noticias(request):
    if request.method == "POST":
         formulario = NoticiaFormulario(request.POST)

         if formulario.is_valid():
             data = formulario.cleaned_data
             noticia = Noticias(
                 titulo=data['titulo'], 
                 subtitulo=data['subtitulo'], 
                 cuerpo=data['cuerpo'],
                 fecha_publicacion=data['fecha_publicacion'], 
                 autor=data['autor'],
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

def buscar_noticias(request):
    if request.method == "POST":
        data = request.POST
        noticias = Noticias.objects.filter(fecha_publicacion__exact=data['fecha_publicacion']) 
        contexto = {
            'noticias' : noticias
        }
        return render(
            request=request,
            template_name= 'pagina_blog/lista_noticias.html',
            context = contexto 
        )

@login_required
def ver_noticia(request, id):
    noticia = Noticias.objects.get(id=id)
    contexto = {
        'noticia' : noticia 
    }
    return render(
        request=request,
        template_name='pagina_blog/ver_noticia.html',
        context = contexto
    )

@login_required
def editar_noticia(request, id):
    noticia = Noticias.objects.get(id=id)
    if request.method == "POST":
        formulario = NoticiaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            noticia.titulo=data['titulo'] 
            noticia.subtitulo=data['subtitulo'] 
            noticia.cuerpo=data['cuerpo']
            noticia.fecha_publicacion=data['fecha_publicacion'] 
            noticia.autor=data['autor']
            noticia.save()
            url_exitosa = reverse('listar_noticias')
            return redirect(url_exitosa)
    else: 
        inicial = {
            'titulo' : noticia.titulo,
            'subtitulo' : noticia.subtitulo,
            'fecha_publicacion' : noticia.fecha_publicacion,
            'autor' : noticia.autor,
        }
        formulario = NoticiaFormulario(initial=inicial)
    return render(
        request=request,
        template_name='pagina_blog/form_noticias.html',
        context={'formulario': formulario, 'noticia': noticia, 'es_update': True},
    )

def mi_info(request):
    return render(
        request=request,
        template_name='pagina_blog/about.html'
        )

class NoticiaDeleteView(LoginRequiredMixin,DeleteView):
    model = Noticias
    success_url = reverse_lazy('listar_noticias')
    template_name = 'pagina_blog/confirmacion.html'