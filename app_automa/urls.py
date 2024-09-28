from django.urls import path
from app_automa import views
from .views import listar, logout

urlpatterns = [
    path('', views.home, name='home'), 
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('servicos/', views.servicos, name='servicos'),
    path('logout/', logout, name='logout'),




#______________  VER O CADASTRO _________________________
    path('listar/', listar.as_view(), name='orcamento'),

#______________     CRIAR UM CADASTRO _________________________
    path('solicitar/', views.pedidosCreateView.as_view(), name='solicitar'),


#______________ ATUALIZAR CADASTRO  ___________________
    path('editar/<int:pk>/', views.pedidosUpdadeView.as_view(), name='editar-pedido'),


#______________ EXCLUIR CADASTRO  ___________________
    path('excluir/<int:pk>', views.pedidoDelete.as_view(),name='excluir-pedido')
]   