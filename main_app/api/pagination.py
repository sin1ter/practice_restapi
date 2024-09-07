from rest_framework.pagination import PageNumberPagination

class TodoListPagination(PageNumberPagination):
    page_size = 10
    ordering = 'tasks'