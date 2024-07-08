from django.shortcuts import render,redirect
from fbvApp.models import Todo
from fbvApp.forms import TodoForm
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def gettasks(request):
    tasks= Todo.objects.all()
    return render(request,'fbvApp/index.html',{'tasks':tasks})

@login_required
def createtasks(request):
    form = TodoForm()
    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render (request,'fbvApp/create.html',{'form':form})

@login_required
@permission_required('fbvApp.delete_todo')
def  deletetasks(request,id):
    tasks = Todo.objects.get(id=id)
    tasks.delete()
    return redirect('/')

@login_required
def updatetasks(request,id):
    tasks=Todo.objects.get(id=id)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'fbvApp/update.html',{'tasks':tasks})

def logout(request):
    return render(request,'fbvApp/logout.html')