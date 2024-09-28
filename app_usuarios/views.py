
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Perfil
from django.core.mail import send_mail
from django.contrib.auth.forms import UserChangeForm
from .forms import UserUpdateForm


#____________________ CRIAR USUÁRIO _______________________
class UsuarioCreate(CreateView):
    template_name = "usuarios/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super(UsuarioCreate, self).form_valid(form)

        send_mail(
            'Bem-vindo ao nosso site!',
            'Obrigado por se registrar.',
            'from@example.com',
            [form.instance.email],  # Use the email from the form
            fail_silently=False,
        )

        return response


#____________________ ATUALIZAR USUÁRIO _______________________
class PerfilUpdate(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'usuarios/form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    


    