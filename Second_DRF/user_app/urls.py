from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import Registar,Logout

urlpatterns = [
    path('login/',obtain_auth_token, name='login'),
    path('registar/',Registar.as_view(),name ='registar'),
    path('logout/',Logout.as_view(),name='logout')
]

