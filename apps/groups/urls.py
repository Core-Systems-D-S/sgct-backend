from django.urls import path
from .views import GroupAPIView
urlpatterns = [
    path('createGroup/', GroupAPIView.as_view(), name = "create_group")
]

