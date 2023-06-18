from django.db import models
from django import forms
# Create your models here.
class BookShopModel(models.Model):
    genre = [('thriller','thriller'),('fiction','fiction'), ('poem','poem'), ('religious','religious'),('academic','academic')]
    book_id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    book_author= models.CharField(max_length=30)
    book_genre = models.CharField(max_length=30,choices=genre)
    pub_date = models.DateField()
    