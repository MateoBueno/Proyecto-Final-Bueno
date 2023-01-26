from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from usuarios.forms import UserRegisterForm

def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='usuarios/registro.html',
        context={'form':formulario},
    )

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)

            if user:
                login(request=request, user=user)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else: 
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='usuarios/login.html',
        context={'form':form},
    )
    
class CustomLogoutView(LoginRequiredMixin,LogoutView):
    template_name = 'usuario/logout.html'
    next_page = reverse_lazy('inicio')