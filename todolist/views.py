from django.shortcuts import render
from .forms import TaskForm
from todolist.models import Task
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/todolist/login/')

# Showing To-do List function
def show_todolist(request):
    data_todolist = Task.objects.filter(user=request.user)
    context = {
        'list': data_todolist,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

# Creating a new task function
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = datetime.datetime.now()
        user = request.user
        is_finished = "❎"
        Task.objects.create(title=title, description=description, date=date, user=user, is_finished=is_finished)
        return redirect('todolist:todolist')
    return render(request,"create-task.html")

def create_task_json(request):
    if request.method == "POST":
        user = request.user;
        title = request.POST.get("title")
        description = request.POST.get("description")
        new_obj = Task(user=request.user, title=title, description=description, date=datetime.datetime.now(), is_finished="False")
        new_obj.save();
        return HttpResponse(b"CREATED",status=201)
    
    return HttpResponse("only POST method allowed!");

def get_todolist_json(request):
    if request.method == "GET":
        data = Task.objects.filter(user=request.user);
        return HttpResponse(serializers.serialize("json", data));
    return HttpResponse("Only GET method allowed!");

# Handling register function
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# Handle login function
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:todolist")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    
    return render(request, 'login.html', context)

# Handling logout function
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

# Handling the the task status change
def finish_task(request, pk):
    task = Task.objects.get(id=pk)
    task.is_finished = "✅"
    task.save()
    return redirect('todolist:todolist')

# Deleting task function
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    Task.delete(task)
    return redirect('todolist:todolist')

# Deleting task (AJAX)
def delete_task_ajax(request, id):
    query = Task.objects.filter(pk=id, user=request.user).delete();
    return HttpResponse("Berhasil menghapus task!")    