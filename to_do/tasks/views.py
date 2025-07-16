from django.shortcuts import render
from django.db.models import Q
from .models import Task
from .forms import TaskForm


query = ''
show_all = True

# Create your views here.
def home(request):
    global show_all
    show_all = True
    tasks = Task.objects.filter()
    form = TaskForm()
    show_button = 'view completed' if show_all else 'view all'
    context = {'tasks':tasks, 'form':form, 'show_button':show_button}
    return render(request, 'tasks/index.html', context)

def search_tasks(request):
    global query, show_all
    query = request.GET.get('q', '') 
    show_button = 'view completed' if show_all else 'view all'

    tasks = Task.objects.filter(
        Q(title__icontains=query) |
        Q(deadline__icontains=query)
    )


    context = {'tasks':tasks, 'show_button':show_button}
    return render(request, 'tasks/task-section.html', context)

def add_task(request):
    show_button = 'view completed' if show_all else 'view all'

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            tasks = Task.objects.all()

            response = render(request, 'tasks/task-section.html', {'tasks':tasks, 'show_button':show_button})
            response['HX-Trigger'] = 'success'
            return response
        else:
            context = {'form':form}
            return render(request, 'tasks/add_task_modal.html', context)
        
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    show_button = 'view completed' if show_all else 'view all'


    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            
            if query == '':
                tasks = Task.objects.all()
            else:
                tasks = Task.objects.filter(
                    Q(title__icontains=query) |
                    Q(deadline__icontains=query)
                )

            response = render(request, 'tasks/task-section.html', {'tasks':tasks, 'show_button':show_button})                
            response['HX-Trigger'] = 'update_success'
            return response

    context = {'form':form, 'task':task}
    response = render(request, 'tasks/update_task_modal.html', context)
    response['HX-Trigger'] = 'update_clicked'
    return response

def task_completed(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    response = render(request, 'tasks/task-item.html', {'task':task}) 
    return response
        
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    show_button = 'view completed' if show_all else 'view all'
    context = {'task': task}


    if request.method == 'POST': 
        task.delete()
        tasks = Task.objects.all()
        return render(request, 'tasks/task-section.html', {'tasks':tasks, 'show_button':show_button})
    else:
        response = render(request, 'tasks/delete_modal.html', context)
        response['HX-Trigger'] = 'success'
        return response
        
def view_completed(request):
    global show_all
    global query
    if show_all:
        tasks = Task.objects.filter(is_completed=True)
        show_all = not show_all
    else:
        tasks = Task.objects.all()
        show_all = not show_all
        query = ''


    show_button = 'view completed' if show_all else 'view all'
    context = {'tasks':tasks, 'show_button':show_button}
    return render(request, 'tasks/task-section.html', context)

    
 