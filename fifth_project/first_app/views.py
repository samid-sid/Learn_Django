from django.shortcuts import render,redirect
from . form import Test_form,Password_validation
def Home(request):
    
    
    return render(request,'./first/home.html')
  

def About(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        eml = request.POST.get('email')
        sel = request.POST.get('select')
        return render(request,'./first/about.html',{'name':name, 'email':eml,'select':sel})
    return render(request,'./first/about.html')


def Form(request):
    return render(request,'./first/form.html')


def django_form(request):
    if request.method == 'POST':
        form = Test_form(request.POST,request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open ('./first_app/upload/' + file.name, 'wb+') as des:
            #     for chunk in file.chunks():
            #         des.write(chunk)
            print(form.cleaned_data)
            # return render(request,'./first/django_form.html',{'Form':form})
        
    else:
        form = Test_form()
    return render(request,'./first/django_form.html',{'Form':form})


def password_check(request):
    if request.method == 'POST':
        form  = Password_validation(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    
    else:
        form = Password_validation()
    
    return render(request,'./first/django_form.html',{'Form':form})


