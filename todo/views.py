from django.shortcuts import render, redirect
from .models import Task

def home(request):

    if request.method == "POST":

        title = request.POST.get('title')

        category = request.POST.get('category')

        due_date = request.POST.get('due_date')

        Task.objects.create(
            title=title,
            category=category,
            due_date=due_date
        )

        return redirect('/')

    tasks = Task.objects.all().order_by('due_date')

    health_count = Task.objects.filter(category='Health').count()
    work_count = Task.objects.filter(category='Work').count()
    study_count = Task.objects.filter(category='Study').count()
    personal_count = Task.objects.filter(category='Personal').count()

    context = {
        'tasks': tasks,
        'health_count': health_count,
        'work_count': work_count,
        'study_count': study_count,
        'personal_count': personal_count,
    }

    return render(request, 'home.html', context)


def completeTask(request, id):

    task = Task.objects.get(id=id)

    task.completed = True

    task.save()

    return redirect('/')


def deleteTask(request, id):

    task = Task.objects.get(id=id)

    task.delete()

    return redirect('/')