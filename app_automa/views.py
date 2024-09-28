from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import pedidos
from django.views.generic.list import ListView
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')

def contato(request):
    return render(request, 'contato.html')



#______________  VER O CADASTRO _________________________

class listar(ListView):
    model = pedidos
    template_name = 'crud/listar.html'
    context_object_name = 'pedidos'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return pedidos.objects.all()
        else:
            return pedidos.objects.filter(usuario=self.request.user)

#______________    CRIAR PEDIDO NOVO ___________________

class pedidosCreateView(CreateView):
    model = pedidos
    fields = ['nome', 'email', 'telefone', 'mensagem', 'tipo']
    template_name = 'crud/solicitar.html'
    success_url = '/listar/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        response = super(pedidosCreateView, self).form_valid(form)

        # Create the email body
        email_body = (
            f'Olá {form.instance.nome},\n\n'
            f'Recebemos seu pedido com sucesso!\n'
            f'Detalhes do seu pedido:\n'
            f'Nome: {form.instance.nome}\n'
            f'E-mail: {form.instance.email}\n'
            f'Telefone: {form.instance.telefone}\n'
            f'Mensagem: {form.instance.mensagem}\n'
            f'Tipo: {form.instance.tipo}\n\n'
            f'Não se preocupe, nosso time de especialistas entrará em contato com você em breve com mais detalhes sobre o seu pedido.'
        )

        send_mail(
            'Pedido registrado com sucesso!',
            email_body,
            'from@example.com',
            [form.instance.email],  # Use the email from the form
            fail_silently=False,
        )

        return response

    

#______________ ATUALIZAR PEDIDO ATUAL ___________________
    
class pedidosUpdadeView(UpdateView):
    model = pedidos
    fields = ['nome', 'email', 'telefone', 'mensagem', 'tipo']
    template_name = 'crud/solicitar.html'
    success_url = '/listar/'


#______________ EXCLUIR PEDIDO ATUAL ___________________

class pedidoDelete(DeleteView):
    model = pedidos
    template_name = 'crud/excluir.html'
    success_url = '/listar/'



#______________  LOGOUT _________________________
def logout(request):
    # ...
    auth_logout(request)
    return redirect('/')
