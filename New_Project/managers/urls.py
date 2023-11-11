from django.urls import path
from .views import CreateView, PostsUserView, ViewModel, DeleteView, ReadView, UpdateView


urlpatterns = [
    path('create/', CreateView.as_view(), name='create_view'),
    path('users', PostsUserView.as_view()),
    path('list', ReadView.as_view(), name='list_view'),
    path('view', ViewModel.as_view(), name='view_model'),
    path('delete', DeleteView.as_view(), name='delete_view'),
    path('update', UpdateView.as_view(), name='update_view'),
]