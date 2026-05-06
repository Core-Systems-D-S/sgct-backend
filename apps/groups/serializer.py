from rest_framework import serializers
from apps.groups.models import Group
from apps.users.serializers import UserGroupSerializer

class GroupSerializer(serializers.ModelSerializer):
    owner = UserGroupSerializer(read_only = True)
    
    class Meta:
        model = Group
        fields = ["id", "name", "description", "owner", "is_active"]
        read_only_fields = ["id"]