from django.db import models
from apps.users.models import User
from django.core.validators import MinLengthValidator
from sgtc.choices import roles

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True, )
    is_active = models.BooleanField()


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    role = models.CharField(choices = roles)
    joined_at = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'group')

