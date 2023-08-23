
from django.urls import path
from app_cad import views

urlpatterns = [
    # Rota, view responsável, nome de referência
    # usuarios.com
    path('', views.home,name='home'),
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]
