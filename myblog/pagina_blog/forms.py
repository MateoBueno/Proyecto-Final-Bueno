from django import forms
from pagina_blog.models import Noticias 

# class NoticiaFormulario(forms.Form):
#     titulo = forms.CharField(max_length=256)
#     subtitulo = forms.CharField(max_length=1000)
#     cuerpo = forms.CharField(max_length=1000, widget=forms.Textarea())
#     fecha_publicacion = forms.DateField(required=True)
#     autor = forms.CharField(max_length=64)
#     imagen = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'multiple': True}))

class NoticiaFormulario(forms.ModelForm):
    cuerpo = forms.CharField(max_length=1000, widget=forms.Textarea())
    fecha_publicacion = forms.DateField(required=True)

    class Meta:
        model = Noticias
        fields = ['titulo','subtitulo','cuerpo','fecha_publicacion','autor','imagen']

class EditNoticiasForm(forms.ModelForm):
    cuerpo = forms.CharField(max_length=1000, widget=forms.Textarea())
    fecha_publicacion = forms.DateField(required=True)

    class Meta:
        model = Noticias
        fields = ['titulo','subtitulo','cuerpo','fecha_publicacion','autor','imagen']
