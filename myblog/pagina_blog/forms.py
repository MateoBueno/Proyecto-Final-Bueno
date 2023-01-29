from django import forms
from pagina_blog.models import Noticias 

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
