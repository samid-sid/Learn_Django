from django.urls import path

from . import views

urlpatterns = [
    path('',views.Base.as_view(),name = 'base'),
    path('home/',views.My_view.as_view(),{'author':'Phitron'},name='home'),
    path('book_details/<int:book_id>/',views.Book_details.as_view(),name = 'book_details'),
    # path('home/',views.Home, name = 'home'),
    
    # path('show-books/',views.show_books, name = 'show_books'),
    path('show-books/',views.show_book_list.as_view(), name = 'show_books'),
    
    # path('add-books/',views.Add_books, name='add_books'),
    path('add-books/',views.Add_books.as_view(), name='add_books'),
    
    # path('edit-books/<int:id>/',views.edit_books,name='edit_books'),
    path('edit-books/<int:pk>/',views.edit_books.as_view(),name='edit_books'),
    
    # path('delete-books/<int:id>/',views.delete_books,name='delete_books'),
    path('delete-books/<int:pk>/',views.delete_books.as_view(),name='delete_books'),
]
