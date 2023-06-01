from django.shortcuts import render, redirect, get_object_or_404
from appshot.models import TodoList, TodoItem
from appshot.forms import TodoListForm, TodoItemForm

# Create your views here.


def todo_list(request):
    todo_lists = TodoList.objects.all()
    context = {"todo_lists": todo_lists}
    return render(request, "todos/todos.html", context)


def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    tasks = todo_list.items.all()
    context = {"todo_list": todo_list, "tasks": tasks}
    return render(request, "todos/todo_list_detail.html", context)


def todo_list_create(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos:todo_list_list")
    else:
        form = TodoListForm()
        context = {"form": form}
        return render(request, "todos/todo_list_create.html", context)


def todo_list_update(request, id):
    post = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        form = TodoListForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("todos:todo_list_detail", id=id)
    else:
        form = TodoListForm(instance=post)
    context = {"post_object": post, "form": form}
    return render(request, "todos/todo_list_update.html", context)


def todo_list_delete(request, id):
    post = get_object_or_404(TodoList, id=id)
    if request.method == "POST":
        post.delete()
        return redirect("todos:todo_list_list")

    context = {"post_object": post}
    return render(request, "todos/todo_list_delete.html", context)


def todo_item_create(request):
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos:todo_list_list")
        else:
            print("Form is not valid:", form.errors)
    else:
        form = TodoItemForm()

    todo_lists = TodoList.objects.all()
    context = {"form": form, "todo_lists": todo_lists}
    return render(request, "todos/todo_item_create.html", context)
