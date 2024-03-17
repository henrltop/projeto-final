from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import pedidos
from django.views.generic.list import ListView

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')

def contato(request):
    return render(request, 'contato.html')



#______________  VER O CADASTRO _________________________

class listar (ListView):
    model = pedidos
    template_name = 'crud/listar.html'

#______________    CRIAR CADASTRO NOVO ___________________

class pedidosCreateView(CreateView):
    model = pedidos
    fields = ['nome', 'email', 'telefone', 'mensagem', 'tipo']
    template_name = 'crud/solicitar.html'
    success_url = '/listar/'


#______________ ATUALIZAR CADASTRO ATUAL ___________________
    
class pedidosUpdadeView(UpdateView):
    model = pedidos
    fields = ['nome', 'email', 'telefone', 'mensagem', 'tipo']
    template_name = 'crud/solicitar.html'
    success_url = '/listar/'


#______________ EXCLUIR CADASTRO ATUAL ___________________

class pedidoDelete(DeleteView):
    model = pedidos
    template_name = 'crud/excluir.html'
    success_url = '/listar/'

