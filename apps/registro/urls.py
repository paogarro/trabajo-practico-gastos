from django.urls import path
from .views import RegistroListView, RegistroCreateView, RegistroUpdateView, RegistroDeleteView

urlpatterns = [
    path('', RegistroListView.as_view(), name='registro_list'),
    path('nuevo/', RegistroCreateView.as_view(), name='registro_create'),
    path('<int:pk>/editar/', RegistroUpdateView.as_view(), name='registro_update'),
    path('<int:pk>/eliminar/', RegistroDeleteView.as_view(), name='registro_delete'),
]
