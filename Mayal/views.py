from django.shortcuts import render

from Mayal.models import *
from Mayal.forms import *
from django.views.generic.edit import View, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.contrib import messages
from django.shortcuts import render, redirect, render,get_object_or_404
from django.urls import reverse_lazy, reverse

# Create your views here.
def index(request):
    context = {}
    return render(request, 'administrador/base.html', context)


# CRUD ------ CATEGORIA------------------------------------------------------------------------------------
class ListarCategorias(ListView):
    model = Categoria
    template_name = 'CRUDs/Categoria/lista.html'
    context_object_name = 'categorias'

class CrearCategoria(CreateView):
    model = Categoria
    template_name = 'CRUDs/Categoria/crear.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('listar_categorias')

class ModificarCaategoria(UpdateView):
    model = Categoria
    template_name = 'CRUDs/Categoria/crear.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('listar_categorias')

def borrarCategoria(request, id):
    cat = get_object_or_404(Categoria, id=id)

    cat.delete()
    messages.success(request, " Categoria eliminado correctamente")
    return redirect(to="listar_categorias")

# CRUD ------ SUBCATEGORIA----------------------------------------------------------------------------------
class ListarSubcategorias(ListView):
    model = Subcategoria
    template_name = 'CRUDs/Subcategoria/lista.html'
    context_object_name = 'subcategorias'

class CrearSubcategoria(CreateView):
    model = Subcategoria
    template_name = 'CRUDs/Subcategoria/crear.html'
    form_class = SubcategoriaForm
    success_url = reverse_lazy('listar_categorias')

class ModificarCategoria(UpdateView):
    model = Subcategoria
    template_name = 'CRUDs/Subcategoria/crear.html'
    form_class = SubcategoriaForm
    success_url = reverse_lazy('listar_categorias')

def borrarSubcategoria(request, id):
    cat = get_object_or_404(Subcategoria, id=id)

    cat.delete()
    messages.success(request, " Subcategoria eliminado correctamente")
    return redirect(to="listar_categorias")