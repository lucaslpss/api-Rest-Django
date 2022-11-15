from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa
from .forms import PessoaForm


class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('login')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user)
        filtro_login = self.request.GET.get('login') or None

        if filtro_login:
            queryset = queryset.filter(login__contains=filtro_login)
        return queryset


class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoas/'


class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoas/'
