import tabnanny
from django.shortcuts import render, redirect
from .forms import RegistarForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def Home(request):
    return render(request, 'home.html')


def login_page(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=name, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'Form': form})
    else:
        return redirect('profile')


def signup(request):
    try:
        if not request.user.is_authenticated:
            if request.method == 'POST':
                form = RegistarForm(request.POST)
                if form.is_valid():
                    messages.success(request, "Account Created SuccessFully.")
                    form.save()
            else:
                form = RegistarForm()
            return render(request, 'signup.html', {'Form': form})
        else:
            return redirect('logout')
    except TypeError as t:
        print(t)


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Updated Successfully")
            return redirect('profile')

    else:
        form = ChangeUserData(instance = request.user)
    return render(request,'profile.html',{'Form':form})


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='profile')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Change Successfully")
            return redirect('change_pass')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_pass.html', {'Form': form})


@login_required(login_url='profile')
def change_password2(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Change Successfully")
            return redirect('change_pass2')

    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'change_pass.html', {'Form': form})


# def Update_user(request):
#     if request.method == 'POST':
#         form = ChangeUserData(request.POST, instance = request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Account Updated Successfully")
#             return redirect('profile')
    
#     else:
#         form = ChangeUserData(instance = request.user)
#     return render(request,'profile.html',{'Form':form})
