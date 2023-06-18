from django.db import models
from django.contrib.auth.models  import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='review')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.IntegerField(choices=[(i,i) for i in range(1,6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('product','user')
        
    def __str__(self) -> str:
        return f"Product: {self.product.name} Rating : {self.rating} User:{self.user.username}"
        # return f"Desc : {self.description} --------- Rating: {self.rating}"