from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import BookStoreForm
from django.contrib import messages
from django.urls import reverse,reverse_lazy
from .models import BookShopModel
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView

# Create your views here.


class Base(TemplateView):
    template_name = 'base.html'
    

# def Home(request):
#     return render(request, 'home.html')

class My_view(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context = {'Name':'Samid Sid','Age':22}
        context.update(kwargs)
        return context
    


# def show_books(request):
#     book = BookShopModel.objects.all()
#     return render(request, 'show_books.html',{'data':book})

class show_book_list(ListView):
    model = BookShopModel
    template_name = 'show_books.html'
    context_object_name = 'data'
    # def get_queryset(self):
    #     return BookShopModel.objects.filter(book_author = 'Humayon')
    # ordering = ['book_author']
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = {'data':BookShopModel.objects.all().order_by('book_id')}
        return context


class Book_details(DetailView):
    model = BookShopModel
    template_name = 'book_details.html'
    context_object_name = 'item'
    pk_url_kwarg = 'book_id'
    

# def Add_books(request):
#     if request.method == 'POST':
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#         messages.success(request, 'Book Added Successfully')
#         return HttpResponseRedirect(reverse('add_books'))
#         # return redirect('/add-books/')
#     else:
#         book = BookStoreForm()
#     return render(request, 'add_book.html', {'form': book})


# class Add_books(FormView):
#     form_class = BookStoreForm
#     template_name = 'add_book.html'
#     success_url = reverse_lazy('add_books')
    
#     def form_valid(self, form: Any):
#         form.save()
#         return redirect('show_books')

class Add_books(CreateView):
    model = BookShopModel
    form_class = BookStoreForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('add_books')
    
    

# def edit_books(request,id):
#     book = BookShopModel.objects.get(pk=id)
#     form = BookStoreForm(instance=book)
    
#     if request.method == 'POST':
#         form = BookStoreForm(request.POST,instance=book)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Update SuccessFull')
#             return redirect('home')
    
#     return render(request,'add_book.html',{'form':form})

class edit_books(UpdateView):
    model = BookShopModel
    form_class = BookStoreForm
    template_name = 'add_book.html'
    success_url = reverse_lazy('show_books')
    

# def delete_books(request,id):
#     BookShopModel.objects.get(pk=id).delete()
#     return redirect('home')

class delete_books(DeleteView):
    model = BookShopModel
    template_name = 'delete_book.html'
    success_url = reverse_lazy('show_books')
    