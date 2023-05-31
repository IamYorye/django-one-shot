from django.urls import path
from appshot.views import todo_list, todo_list_detail

app_name = "todos"

urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", todo_list_detail, name="todo_list_detail"),
]
