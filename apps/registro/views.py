from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Registro

class RegistroListView(ListView):
    model = Registro
    template_name = 'registro/list.html'
    context_object_name = 'registros'

class RegistroCreateView(CreateView):
    model = Registro
    fields = ['total', 'fecha', 'tipo', 'categoria']
    template_name = 'registro/create.html'
    success_url = reverse_lazy('registro_list')

class RegistroUpdateView(UpdateView):
    model = Registro
    template_name = 'registro/update.html'
    fields = ['total', 'fecha', 'tipo', 'categoria']
    success_url = reverse_lazy('registro_list')

class RegistroDeleteView(DeleteView):
    model = Registro
    template_name = 'registro/delete.html'
    success_url = reverse_lazy('registro_list')