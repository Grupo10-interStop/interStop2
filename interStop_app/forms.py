from django import forms

class formulario_datos(forms.Form):

    problema=forms.CharField()
    sector=forms.CharField()
    comentario=forms.CharField()

  