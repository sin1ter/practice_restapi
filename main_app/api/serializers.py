from rest_framework import serializers

from main_app.models import *

class TodoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        exclude = ['owner']

