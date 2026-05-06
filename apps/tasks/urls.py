from django.urls import path
from .views import TaskAPIView, TaskCommentAPIView

urlpatterns = [
    path("", TaskAPIView.as_view(), name = "tasks"),
    path("<int:pk>/", TaskAPIView.as_view(), name = "one_task"),
    path("comment/", TaskCommentAPIView.as_view(), name = "comment")
]