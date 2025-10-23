from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=120, label="Nombre completo")
    email = forms.EmailField(label="Email")
    asunto = forms.CharField(max_length=150, label="Tema")
    mensaje = forms.CharField(widget=forms.Textarea, label="Mensaje")
