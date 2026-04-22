from rest_framework import serializers
from apps.tasks.models import Tasks
from apps.groups.serializer import GroupSerializer
from apps.categories.serializer import CategorySerializer
from apps.users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):

    group = GroupSerializer()
    category = CategorySerializer()
    created_by = UserSerializer()
    assigned_to = UserSerializer()

    class Meta:
        model = Tasks
        fields = [
            "title", 
            "description",  
            "status", 
            "priority", 
            "group", 
            "category",
            "created_by", 
            "assigned_to", 
            "due_date"
        ]
