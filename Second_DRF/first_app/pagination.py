from rest_framework.pagination import PageNumberPagination,CursorPagination

class Product_Pagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size =5
    
    
class Product_Cursor_Pagination(CursorPagination):
    page_size = 3
    cursor_query_param = 'c'
    ordering =['-price']