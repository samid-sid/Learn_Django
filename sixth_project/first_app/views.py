from django.shortcuts import render,redirect
from . import models
from .models import Teacher,Student
from .forms import Registration_Form
from django.contrib import messages
# Create your views here.
def Home(request):
    data = models.Student.objects.all()
    context= { 'data':data
    }
    return render(request,'home.html',context)


def Delete_student(request,id):
    
    obj = models.Student.objects.get(pk = id).delete()
    
    return redirect('homepage')
    


def Registar(request):
    if request.method == 'POST':
        form = Registration_Form(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            messages.success(request,'Ragistrarion Successful.')
    else:
        form = Registration_Form()
    return render(request,'registar.html',{'Form':Registration_Form()})


def showData(request):
    # teachers = Teacher.objects.get(name='Raihan')
    # students = teachers.student.all()
    
    # for stu in students:
    #     print(stu.name)
    
    student = Student.objects.get(name ='Emon Ahmed')
    teachers = student.Teachers.all()
    
    for t in teachers:
        print(t.name)
        
    return render(request,'home.html')
    
    