from django.shortcuts import render

from Mayal.models import *
from Mayal.forms import *
from django.views.generic.edit import View, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, render,get_object_or_404
from django.urls import reverse_lazy, reverse

# Create your views here.
def index(request):
    context = {}
    return render(request, 'administrador/base.html', context)

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

class BorrarCategoria(DeleteView):
    template_name = 'CRUDs/Categoria/borrar.html'
    model = Categoria
    success_url = reverse_lazy('listar_categorias')

def borrarCategoria(request, pk):
    cat = Categoria.objects.filter(id = pk).first()

    if request.method == 'POST':
        cat.delete()

        return redirect('listado_horarios')