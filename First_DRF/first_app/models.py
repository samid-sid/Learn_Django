from django.db import models

# Create your models here.

class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    student  = models.ForeignKey(Students,on_delete=models.CASCADE,related_name='course',default=None)
    course_name = models.CharField(max_length=30)
    marks = models.IntegerField()
    
    def __str__(self):
        return  f" {self.course_name} : {self.marks}"