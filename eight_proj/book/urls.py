from django.urls import path
from . import views

urlpatterns = [
    # path('',views.TemplateView.as_view(template_name = './book/home.html')),
    path('',views.set_session,name = 'home'),
    path('get/',views.get_session,name = 'get'),
    path('del/',views.del_session,name = 'del'),
]
