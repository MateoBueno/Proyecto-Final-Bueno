from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from pagina_blog.models import Noticias
from pagina_blog.forms import EditNoticiasForm, NoticiaFormulario



def inicio(request):
    return render(
        request=request,
        template_name='pagina_blog/inicio.html'
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


class NoticiaCreateView(LoginRequiredMixin, CreateView):
    model = Noticias 
    form_class = NoticiaFormulario
    success_url = reverse_lazy('listar_noticias')
    template_name = 'pagina_blog/form_noticias.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(NoticiaCreateView, self).form_valid(form)


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


class NoticiaEditView(LoginRequiredMixin, UpdateView):
    model = Noticias 
    form_class = EditNoticiasForm
    success_url = reverse_lazy('listar_noticias')
    template_name = 'pagina_blog/editar_noticias.html'


def mi_info(request):
    return render(
        request=request,
        template_name='pagina_blog/about.html'
        )


class NoticiaDeleteView(LoginRequiredMixin,DeleteView):
    model = Noticias
    success_url = reverse_lazy('listar_noticias')
    template_name = 'pagina_blog/confirmacion.html'