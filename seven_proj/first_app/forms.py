from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class RegistarForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email']
        
        
class ChangeUserData(UserChangeForm):
    password = None
    class Meta:
        model = User 
        fields = ['username','first_name','last_name','email']
        
    
    