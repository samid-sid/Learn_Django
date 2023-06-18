from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='homepage'),
    path('about/',views.About,name='aboutpage'),
    path('form/',views.Form,name='formpage'),
    path('django-form/',views.password_check,name='django_form_page'),
]
