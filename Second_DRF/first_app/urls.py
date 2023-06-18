from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import Product_view, Review_view

router = DefaultRouter()
router.register('products',viewset= Product_view,basename='products')
router.register('reviews',viewset=Review_view,basename='reviews')



urlpatterns = [
    path('',include(router.urls)),
    path('api/',include('rest_framework.urls')),
]