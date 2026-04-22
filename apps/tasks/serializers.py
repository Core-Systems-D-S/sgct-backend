from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from django.contrib.auth import get_user_model

from .models import Task, TaskComent
from apps.groups.models import Group, UserGroup
from apps.categories.models import Category
from apps.users.serializers import UserSerializer
User = get_user_model()

class TaskSerializer(serializers.ModelSerializer):
    group = PrimaryKeyRelatedField(queryset = Group.objects.all())
    category = PrimaryKeyRelatedField(queryset = Category.objects.all())
    assigned_to = PrimaryKeyRelatedField(queryset = User.objects.all())
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Task
        fields = "__all__"

    def validate(self, data):

        created_by = self.context["request"].user
        group = data.get("group")
        assigned_to = data.get("assigned_to")

        print(f"user id: {created_by.id}")
        print(f"group id: {group}")

        if not UserGroup.objects.filter(user=created_by, group = group).exists():
            raise serializers.ValidationError("No puedes crear tareas en este grupo.")
        
        if not UserGroup.objects.filter(user = assigned_to, group = group).exists():
            raise serializers.ValidationError("El usuario al que se le asignó la tarea no existe en este grupo.")
        
        return data
    
class TaskComentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    task = PrimaryKeyRelatedField(queryset = Task.objects.all())

    class Meta:
        model = TaskComent
        fields = "__all__"
