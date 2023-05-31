from django.shortcuts import render, redirect, get_object_or_404
from appshot.models import TodoList, TodoItem

# Create your views here.


def todo_list(request):
    todo_lists = TodoList.objects.all()
    context = {"todo_lists": todo_lists}
    return render(request, "todos/todos.html", context)


def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    tasks = TodoItem.objects.filter(list=todo_list)
    context = {"todo_list": todo_list, "tasks": tasks}
    return render(request, "todos/todo_list_detail.html", context)
