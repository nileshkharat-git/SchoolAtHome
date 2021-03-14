from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .models import Accounts
from universities.models import Student
def signUp(request):
    if request.POST:
        f_name=request.POST['first_name']
        l_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        user=Accounts.object.create_user(email,f_name,l_name,password)
        user.save()
        print('user created')
        return redirect('/')
    return redirect('/')

def user_login(request):
    email=request.POST['email']
    password=request.POST['password']
    user=authenticate(request,username=email,password=password)
    if user:
        login(request,user)
        redirect('/')
    return redirect('/')


def user_logout(request):
    logout(request)
    return redirect('/')

def user_dashboard(request):
    user=get_object_or_404(Accounts,email=request.user.email)
    name=f"{user.first_name} {user.last_name}"
    stud=Student.objects.filter(student=user)
    return render(request,'myDashboard.html',{'student':stud,'name':name})
