from django.urls import path

from .views import MainHomePage, ToDoList, ToDoDelete, ToDoUpdate

urlpatterns = [
    path('', MainHomePage.as_view(), name='home'),
    path('todos/', ToDoList.as_view(), name='todos_list'),
    path('todos/<str:pk>/', ToDoDelete.as_view(), name='todos_delete'),
    path('todos/<str:pk>/update/', ToDoUpdate.as_view(), name='todos_update'),
]
