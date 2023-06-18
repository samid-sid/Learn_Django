from django.urls import path
from . import views 

urlpatterns = [
    path('',views.Home,name='homepage'),
    path('registar/',views.Registar,name = 'registar'),
    path('delete/<int:id>',views.Delete_student,name='delete_student'),
    path('show/',views.showData,name = 'show_data'),
]
