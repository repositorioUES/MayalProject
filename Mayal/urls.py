from django.urls import path
from .views import *

urlpatterns = [
    path('administrador', index, name="index"),
    path('listadoCategorias/', ListarCategorias.as_view(), name='listar_categorias'),
    path('crearCategoria', CrearCategoria.as_view(), name="crear_categoria"),
    path('modificarCategoria/<int:pk>', ModificarCategoria.as_view(), name='modificar_categoria'),
    path('borrarCategoria/<id>/',borrarCategoria,name='borrar_categoria'),

    path('listadoSubcategorias/', ListarSubcategorias.as_view(), name='listar_categorias'),
    path('crearSubcategoria', CrearSubcategoria.as_view(), name="crear_subcategoria"),

]