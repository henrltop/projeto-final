from django.urls import path
from .views import home, sobre, contato, servicos

urlpatterns = [
    path('', home.as_view(), name='home'), 
    path('sobre/', sobre.as_view(), name='sobre'),
    path('contato/', contato.as_view(), name='contato'),
    path('servicos/', servicos.as_view(), name='servicos'),
]
