from django.urls import path
from .views import CategoriaListView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView

app_name = 'categoria'
urlpatterns = [
    path('', CategoriaListView.as_view(), name='categoria_list'),
    path('nuevo/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='categoria_delete'),
]