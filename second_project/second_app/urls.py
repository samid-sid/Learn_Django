from django.urls import path
from . import views

urlpatterns = [
    path('course/',views.Course),
    path('feedback/',views.Feedback),
]
