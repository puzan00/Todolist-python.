from django.shortcuts import render,redirect
from .models import Todo
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
        todos = Todo.objects.filter(author=request.user)
        return render(request, 'home.html', {'todos': todos})
   
@login_required
def add(request):
    if request.method =='GET':
        return render(request,'add.html')
    else:
        t=request.POST['title']
        d=request.POST['description']
        Todo.objects.create(title=t,description=d,author_id=request.user.id)
        return redirect('home')
@login_required    
def delete(request,id):
    Todo.objects.get(id=id).delete()
    return redirect('home')
@login_required
def edit(request,id):
    todo=Todo.objects.get(id=id)
    if request.method =='GET':
        return render(request,'edit.html',{'todo':todo})
    else:
        todo.title=request.POST['title']
        todo.description=request.POST['description']
        todo.save()
        return redirect('home')
@login_required    
def delete_all(request):
    Todo.objects.all().delete()
    return redirect('home')
@login_required
def mark_complete(request,id):
     todo=Todo.objects.get(id=id)
     todo.is_completed=not todo.is_completed
     todo.save()
     return redirect('home')