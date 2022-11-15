from django.contrib import admin
from .models import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'login',
        'senha',
        'data_nascimento'
    ]
    search_fields = [
        'login'
    ]

admin.site.register(Pessoa, PessoaAdmin)
