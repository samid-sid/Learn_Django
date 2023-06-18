from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'./data/index.html')

def about(request):
    
    return render(request,'./data/about.html',{'auther':'samid sid'})