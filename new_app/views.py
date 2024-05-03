from django.shortcuts import render, redirect

from new_app.forms import TodoForm
from new_app.models import Todo


# Create your views here.
def home(request):
    return render(request,template_name='home.html')
def index(request):
    return render(request,template_name='index.html')
def index(request):
    return render(request,template_name='index2.html')

def todo(request):
    data =TodoForm()

    if request.method == 'POST':
        msg = TodoForm(request.POST)
        if msg.is_valid():
            msg.save()
            return redirect('views_todo')

    return render(request,'dashboard.html',{'data':data})
def views_todo(request):
    data = Todo.objects.all()
    print(data)
    return render(request, 'views.html', {'data': data})
def delete (request,id):
    data = Todo.objects.get(id=id)
    data.delete()
    return redirect('views_todo')
def update(reguest,id):
    todo= Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if reguest.method == 'POST':
        form = TodoForm(reguest.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect('views_todo')

    return render(reguest,'update.html',{'form':form})
