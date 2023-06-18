from django import forms
from .models import Registration , Student



class Registration_Form(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        labels ={
            'id' : 'Your Id :',
            'name': 'Full Name: ',
            'dob':'Date of Birth : ',
            'contact' : 'Mobile :'
        }
            
        widgets ={
            'id':forms.NumberInput(),
            'dob':forms.DateInput(attrs={'type':'date'})
        }

class Student_form(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
        widgets = {
            'dob' : forms.DateInput(attrs={'type':'date'}),
        }