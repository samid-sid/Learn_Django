from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home,name="home"),   
    path('login/',views.login_page,name="login"),   
    path('signup/',views.signup,name="signup"),   
    path('profile/',views.profile,name="profile"),   
    path('logout/',views.logout_page,name="logout"),
    path('change_password/',views.change_password,name='change_pass'),   
    path('change_password2/',views.change_password2,name='change_pass2')   
]
