from django.urls import path
from .views import *

urlpatterns = [
    path('administrador', index, name="index"),

    path('administrador/listadoCategorias/', ListarCategorias.as_view(), name='listar_categorias'),
    path('administrador/crearCategoria', CrearCategoria.as_view(), name="crear_categoria"),
    path('administrador/modificarCategoria/<int:pk>', ModificarCategoria.as_view(), name='modificar_categoria'),
    path('administrador/borrarCategoria/<int:pk>',borrarCategoria, name='borrar_categoria'),

    path('administrador/listadoSubcategorias/', ListarSubcategorias.as_view(), name='listar_categorias'),
    path('administrador/crearSubcategoria', CrearSubcategoria.as_view(), name="crear_subcategoria"),


]