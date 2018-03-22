from django import forms


class ContactForm(forms.Form):
    Email = forms.EmailField(required=True)
    Email.widget.attrs.update({'type': 'email', 'class': "form-control col-lg-4", 'name': "email"})
    Assunto = forms.CharField(required=True)
    Assunto.widget.attrs.update({'type': 'text', 'class': "form-control col-lg-4", 'name':"assunto"})
    Messagem = forms.CharField(widget=forms.Textarea, required=True)
    Messagem.widget.attrs.update({'class': "form-control col-lg-12", 'name': "message", 'rows': '6'})