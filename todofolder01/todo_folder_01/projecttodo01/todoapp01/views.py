from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapp01.forms import TodoForm
from todoapp01.models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic import UpdateView, DeleteView


# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task_obj01'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task_obj02'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    fields = ('taskName', 'taskPriority', 'taskDate')
    context_object_name = 'task_obj03'

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs= {'pk': self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


def add(request):
    taskobj01 = Task.objects.all()
    if request.method == 'POST':
        task_name = request.POST.get('task_name', '')
        task_priority = request.POST.get('task_priority', '')
        task_date = request.POST.get('task_date', '')

        taskObj = Task(taskName= task_name, taskPriority= task_priority, taskDate= task_date)
        taskObj.save()
    return render(request, 'home.html', {'task_obj01': taskobj01})
#
def delete(request, taskid):
    task = Task.objects.get(id= taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')

def update(request, taskid):
    task = Task.objects.get(id=taskid)
    form_todo = TodoForm(request.POST or None, instance=task)
    if form_todo.is_valid():
        form_todo.save()
        return redirect('/')
    return render(request, 'edit.html', {'taskObj': task, 'formObj': form_todo})