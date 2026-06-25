from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.categoria.models import Categoria

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/list.html'
    context_object_name = 'categorias'

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'categoria/create.html'
    fields = '__all__'
    success_url = reverse_lazy('categoria:categoria_list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'categoria/update.html'
    fields = '__all__'
    success_url = reverse_lazy('categoria:categoria_list')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/delete.html'
    success_url = reverse_lazy('categoria:categoria_list')
