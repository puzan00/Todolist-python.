from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method =='GET':
        return render(request,'register.html')
    else:
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']

        User.objects.create_user(first_name=fn,last_name=ln,username=username, email=email, password=password)
        messages.success(request,'Acount created successfully')
        return redirect('login')
def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u_name=request.POST['username']
        p_word=request.POST['password']
    user=authenticate(username=u_name, password=p_word)

    if user is not None:
        login(request, user)
        next_url=request.GET.get('next')
        if next_url is not None:
            return redirect(next_url)
        return redirect('home')
    else:
        messages.error(request,'Invalid username or password')
        return redirect('login')

def signout(request):
    logout(request)
    return redirect('login')
