from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_empresa/', views.cadastrar_empresa, name="cadastrar_empresa"), # type: ignore
    path('listar_empresas/', views.listar_empresas, name="listar_empresas"),  # type: ignore
    path('empresa/<int:id>', views.empresa, name="empresa"), # type: ignore
]
