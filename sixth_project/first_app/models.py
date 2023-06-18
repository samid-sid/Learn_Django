from django.db import models
from django import forms
# Create your models here.


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    address = models.TextField(max_length=50, null=True)

    def __str__(self):
        return f"{self.id} -- {self.name}"


class Registration(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    dob = models.DateField()
    contact = models.CharField(max_length=11)

    def __str__(self):
        return f"Id: {self.id} -- Name : {self.name}"


class Person(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=12)

    class Meta:
        abstract = True


class Users(Person):
     ch = [('Male','Male'),('Female','Female')]
     id = models.IntegerField(primary_key=True)
     address = models.CharField(max_length=50,default="")
     
     
     def __str__(self):
         return f'Id:{self.id}--Name:{self.name}'
     
     
class Passport(models.Model):
    User = models.OneToOneField(Users,models.PROTECT)
    Passport_No = models.IntegerField(unique=True)
    option = [('48','48'), ('64','64')]
    page = models.CharField(max_length=5,choices=option,default='48')
    validity_ops = [
     ('5','5'),('10','10'),
    ]   
    validity = models.CharField(max_length=5,choices=validity_ops,default="5")
    
     


class Student_info(Person):
    dob = models.DateField()
    result = models.CharField(max_length=5)
    address = models.CharField(max_length=30,null=True)

class Teacher(Person):
    student = models.ManyToManyField(Student,related_name='Teachers')
    subject = models.CharField(max_length=20)
    salary = models.IntegerField()
    Batch = models.CharField(max_length=10 ,null=True)
    
    def student_info(self):
        return ",".join([str(stu) for stu in self.student.all()])

class Friend(Person):
    section = models.CharField(max_length=10)
    attendence = models.BooleanField()
    
    
class Me(Friend):
    class Meta:
        proxy = True
        ordering = ['id']










#      class Manager(Person):
#     take_interview = models.BooleanField()
#     join_date = models.DateField(widgets = forms.DateInput(attrs={'type':'date'}))
