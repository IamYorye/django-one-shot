from django.forms import ModelForm
from appshot.models import TodoList


class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = ("name",)
