from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type": "date"}))
    class Meta:
        model = Pessoa
        fields = ['login', 'senha', 'data_nascimento']
        