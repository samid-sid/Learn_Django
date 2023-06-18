from rest_framework import serializers
from .models import Product,Review


    
    
class Review_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Review 
        fields = '__all__'
        

class Product_Serializer(serializers.ModelSerializer):
    # review = Review_Serializer(many = True,read_only = True)
    review = serializers.StringRelatedField(many= True)
    class Meta:
        model = Product 
        fields = '__all__'