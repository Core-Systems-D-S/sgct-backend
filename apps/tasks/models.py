from django.db import models
from django.conf import settings
from sgtc.choices import status, priorities
from apps.categories.models import Category
from apps.groups.models import Group
class Task(models.Model):


    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=status,
        default=status[0]
    )

    priority = models.IntegerField(
        choices=priorities,
        default=priorities[2]
    )

    group = models.ForeignKey(
        Group, #se puede usar 'group.Group' en caso de error importacion circular leer en notion https://www.notion.so/Custom-User-Model-setting-AUTH_USER_MODEL-modelos-normales-y-buenas-pr-cticas-en-relaciones-347f7aeb6216809bbbc2d6677894da8d
        on_delete=models.CASCADE,
        related_name='tasks'
    )

    category = models.ForeignKey(
        Category,#se puede usar 'categories.Category'
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_tasks'
    )

    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks'
    )

    due_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['group']),
            models.Index(fields=['assigned_to']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title
    
class TaskComent(models.Model):
    content = models.TextField(blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

#Task
# {
#   "title": "Implementar autenticación JWT",
#   "description": "Configurar login con tokens en DRF",
#   "status": "pending",
#   "priority": 2,
#   "group": 1,
#   "category": 3,
#   "created_by": 1,
#   "assigned_to": 2,
#   "due_date": "2026-05-01T18:00:00Z"
# }