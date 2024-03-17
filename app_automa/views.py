from django.views.generic import TemplateView

class home(TemplateView):
    template_name = 'home.html'


class sobre(TemplateView):
    template_name = 'sobre.html'

class servicos(TemplateView):
    template_name = 'servicos.html'

class contato(TemplateView):
    template_name = 'contato.html'

