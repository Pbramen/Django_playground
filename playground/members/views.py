from django.shortcuts import render
from django.http import HttpResponseRedirect

from .form import RegisterForm
from .models import User
from django.forms import ModelForm

# class RegisterForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'user_name', 'email', 'hashword']

def registerForm(request):
    if request.method == 'POST':
        print("form is posting...")
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user_name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            u = User(first_name = first_name, last_name=last_name, user_name=user_name, email=email, hashword = password)
            u.save()
            return HttpResponseRedirect('/members/success/')
    else:
        print("form not yet complete...")
        form = RegisterForm()
    return render(request, 'members/index.html', {"form": form})

def loginForm(request):
    if request.method == 'POST':
        #check if credentials are matching
        if form.is_valid():
            #do something here
            i = 0
        else:
            form = LoginForm()
        return render(request, 'members/login.html', {"form": form})

def success(request):
    return render(request, 'members/success.html', {})