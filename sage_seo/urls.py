# urls.py
from django.urls import path
from .views import RobotsTxtView

urlpatterns = [
    path("robots.txt", RobotsTxtView.as_view()),
]
