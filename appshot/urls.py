from django.urls import path
from appshot.views import (
    todo_list,
    todo_list_detail,
    todo_list_create,
    todo_list_update,
)

app_name = "todos"

urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
    path("create/", todo_list_create, name="todo_list_create"),
    path("<int:id>/edit/", todo_list_update, name="todo_list_update"),
]
