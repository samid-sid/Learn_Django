from django.contrib import admin
from . import models
# from .models import Student_info
# Register your models here.


admin.site.register(models.Student)
admin.site.register(models.Registration)

@admin.register(models.Student_info)
class Student_infoadmin(admin.ModelAdmin):
    list_display = ['id','name', 'address','result']
    
@admin.register(models.Teacher)
class Teacheradmin(admin.ModelAdmin):
    list_display = ['id', 'name','salary','subject','Batch','student_info']
    
    
@admin.register(models.Friend)
class FriendModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','section','attendence','contact']

@admin.register(models.Me)
class MeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','section','attendence','contact']
    
    
@admin.register(models.Users)
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','address','contact']


@admin.register(models.Passport)
class PassportModelAdmin(admin.ModelAdmin):
    list_display = ['User','Passport_No','page','validity']