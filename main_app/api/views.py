
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from main_app.models import *
from main_app.api.serializers import *
from main_app.api.permissions import IsAdminOrReadOnly
from main_app.api.pagination import TodoListPagination

class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoListSerializers
    permission_classes = [IsAuthenticated]
    pagination_class = TodoListPagination

    def get_queryset(self):
        return TodoList.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializers
    permission_classes = [IsAuthenticated]

class NotCompletedTaskView(generics.ListAPIView):
    serializer_class = TodoListSerializers
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return TodoList.objects.filter(owner=self.request.user, not_completed_task=True)
    

class CompletedTaskView(generics.ListAPIView):
    serializer_class = TodoListSerializers
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TodoList.objects.filter(owner=self.request.user, completed_task=True)


class AdminViewOnly(generics.ListAPIView):
    serializer_class = TodoListSerializers
    queryset = TodoList.objects.all()
    permission_classes = [IsAdminUser]