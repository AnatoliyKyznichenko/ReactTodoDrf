from django.shortcuts import render
from django.views import View
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .models import ToDo
from .serializers import ToDoSerializer


class MainHomePage(View):
    template_name = 'base.html'
    
    def get(self, request):
        return render(request, self.template_name)
    
class ToDoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
    
class ToDoDelete(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class ToDoUpdate(generics.UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer


    
    
    
