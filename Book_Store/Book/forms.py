from django import forms
from .models import BookShopModel
class BookStoreForm(forms.ModelForm):
    class  Meta:
       model = BookShopModel
       fields = ['book_id', 'book_name','book_author', 'book_genre', 'pub_date']
    #    exclude =[
    #        'pub_date',
    #    ]
       widgets= {
           'pub_date':forms.DateInput(attrs={'type':'date'})
       }