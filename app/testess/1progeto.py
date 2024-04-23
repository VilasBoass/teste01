from django import forms
from django.core.exceptions import ValidationError

class UsuarioForm(forms.Form):
    nome_usuario:str = forms.CharField(max_length=100)

    def clean_nome_usuario(self):
        nome_usuario = self.cleaned_data.get('nome_usuario')
        if len(nome_usuario) <= 100:
            raise ValidationError("O nome de usuário não pode ter mais de 100 caracteres.")
        return nome_usuario
     nome_usuario:str  = input ('nome do usuario: ')
    print ("nome_usuario ")
