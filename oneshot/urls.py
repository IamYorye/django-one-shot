"""
URL configuration for oneshot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from appshot.views import TodoList


def redirect_to_todo_list_detail(request):
    first_todo_list = TodoList.objects.first()
    if first_todo_list:
        return redirect("todos:todo_list_detail", id=first_todo_list.id)
    else:
        # Handle the case when no TodoList exists
        return redirect("todos:todo_list_list")


urlpatterns = [
    path("", redirect_to_todo_list_detail, name="todo_list_detail"),
    path("admin/", admin.site.urls),
    path("todos/", include(("appshot.urls", "todos"), namespace="todos")),
]
