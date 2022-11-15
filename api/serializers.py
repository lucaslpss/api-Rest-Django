from rest_framework import serializers
from pessoa.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pessoa
        fields = ['login', 'senha', 'data_nascimento']