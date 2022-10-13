from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, finish_task, delete_task, delete_task_ajax, create_task_json, get_todolist_json

app_name = 'todolist'

urlpatterns = [
	path('', show_todolist, name='todolist'),
	path('login/', login_user, name='login'),
	path('register/', register, name='register'),
	path('create-task/', create_task, name='create_task'),
	path('logout/', logout_user, name='logout'),
	path('finished/<int:pk>', finish_task, name='finished'),
	path('deleted/ <int:pk>', delete_task, name='delete'),
	path('delete/<int:id>', delete_task_ajax, name='delete_task_ajax'),
    path('json/', get_todolist_json, name="get_todolist_json"),
    path('add/', create_task_json, name="create_task_json"),
	# path('delete-task/<int:pk>', delete, name='delete_ajax'),
]