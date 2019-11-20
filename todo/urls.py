from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'todos/$', views.todo_list, name='todo_list'),
    url(r'todos/(?P<pk>\d+)', views.note_detail, name='note_detail'),
]
