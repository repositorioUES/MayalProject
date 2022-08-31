from django.shortcuts import render
from Mayal.models import *
from Mayal.forms import *
from django.views.generic.edit import View, UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect, render,get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages

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

class ModificarCategoria(UpdateView):
    model = Categoria
    template_name = 'CRUDs/Categoria/crear.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('listar_categorias')


def borrarCategoria(request, pk):
    categoria = get_object_or_404(Categoria, id=pk)
    categoria.delete()
    messages.success(request, "Categoria eliminada correctamente")
    return redirect(to="listar_categorias")