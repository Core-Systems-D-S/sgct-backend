from django.db import models
from apps.groups.models import Group
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    group= models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add = True)