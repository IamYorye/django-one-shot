from django.shortcuts import render, redirect, get_object_or_404
from appshot.models import TodoList

# Create your views here.


def todo_list(request):
    todo_lists = TodoList.objects.all()
    context = {"todo_lists": todo_lists}
    return render(request, "todos/todos.html", context)
