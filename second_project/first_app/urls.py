from django.urls import path
from . import views

urlpatterns = [
    path('contact/',views.Contact),
    path('about/',views.About),
]
