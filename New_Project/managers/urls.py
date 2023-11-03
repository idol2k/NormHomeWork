from django.urls import path
from .views import CreateView, ReadView, UpdateView, DeleteView


urlpatterns = [
    path('read/', ReadView.as_view(), name='read_view'),
    path('create/', CreateView.as_view(), name='create_view'),
    path('update/', UpdateView.as_view(), name='update_view'),
    path('delete/', DeleteView.as_view(), name='delete_view'),
]