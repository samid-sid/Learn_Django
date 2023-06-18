from django.shortcuts import render
from rest_framework import viewsets,permissions
from .models import Product, Review
from .serializer import Product_Serializer, Review_Serializer
from .permission import ReviewerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import Product_Pagination,Product_Cursor_Pagination

# Create your views here.


class Product_view(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = Product_Serializer
    # filter_backends = [filters.OrderingFilter]
    # search_fields = ['name','description']
    # ordering_fields = ['price']
    pagination_class = Product_Cursor_Pagination
    


class Review_view(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = Review_Serializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['rating','product']
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating']
    
    # def get_queryset(self):
    #     queryset = Review.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is  not None:
    #         queryset = queryset.filter(user__username__icontains = username)
    #     return queryset