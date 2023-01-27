from django import forms 

class NoticiaFormulario(forms.Form):
    titulo = forms.CharField(max_length=256)
    subtitulo = forms.CharField(max_length=1000)
    cuerpo = forms.CharField(max_length=1000, widget=forms.Textarea())
    fecha_publicacion = forms.DateField(required=True)
    autor = forms.CharField(max_length=64)
  