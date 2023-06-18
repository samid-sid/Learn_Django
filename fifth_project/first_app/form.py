from django.core import validators
from django import forms


class Test_form(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(8,message='Max length 8')])
    email = forms.EmailField(validators=[validators.EmailValidator(message='Invalid Email')])
    file = forms.ImageField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png','docs'],message='Invalid file type')], help_text='File must be under 100kb',required=False)
    age = forms.IntegerField(validators=[validators.MinValueValidator(18,message='Age must be greater 18')])
    # balance = forms.DecimalField()
    # birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    # appointment = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    # check = forms.BooleanField()
    # SIZE_CAHT = [('S','SMALL'), ('M','MEDIUM'), ('L','LARGE')]
    # SIZE = forms.ChoiceField(choices=SIZE_CAHT,widget=forms.RadioSelect)
    # data = [('M','Male'),('F','Female'),('O','Others')]
    # gender = forms.MultipleChoiceField(choices=data,widget=forms.CheckboxSelectMultiple)
    

    # def clean(self):
    #     super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']

    #     if(len(valname) < 10 ) :
    #         raise forms.ValidationError('Name must be at least 10char')
    #     if('.com' not in valemail):
    #         raise forms.ValidationError('Invalid Email')
    
class Password_validation(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    
    def clean(self):
        super().clean()
        
        ps = self.cleaned_data['password']
        cps = self.cleaned_data['confirm_password']
        
        if ps != cps :
            raise forms.ValidationError('Password Not Match')