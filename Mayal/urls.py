from django.urls import path
from .views import *

urlpatterns = [
    path('administrador', index, name="index"),
    path('listadoCategorias/', ListarCategorias.as_view(), name='listar_categorias'),
    path('crearCategoria', CrearCategoria.as_view(), name="crear_categoria"),
    path('modificarCategoria/<int:pk>', ModificarCaategoria.as_view(), name='modificar_categoria'),
    path('borrarCategoria/<int:pk>',borrarCategoria,name='borrar_categoria'),

]