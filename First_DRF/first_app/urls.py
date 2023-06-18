from django.urls import path,include
from .views import Student_view,Course_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', viewset=Student_view)
# router.register('course', viewset=Course_view)

urlpatterns = [
    path('',include(router.urls)),
    # path('course/',Course_view.as_view()),
    # path('',Student_view.as_view()), 
    # path('<int:pk>/', Student_Details.as_view()),
    # path('course/<int:pk>/',Course_Details.as_view(),name = 'course_view')   
]
