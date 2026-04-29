from django.urls import path
from .views import GroupAPIView
urlpatterns = [
    path('', GroupAPIView.as_view(), name = "group"),
    path('<int:pk>/', GroupAPIView.as_view(), name = "get_one_group")
]

