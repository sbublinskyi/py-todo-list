from django.urls import path

from todo.views import TaskListView, TagListView

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("tags", TagListView.as_view(), name="tags-list")
]

app_name = "todo"
