from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, finish_task, delete_task

app_name = 'todolist'

urlpatterns = [
	path('', show_todolist, name='todolist'),
	path('login/', login_user, name='login'),
	path('register/', register, name='register'),
	path('create-task/', create_task, name='create_task'),
	path('logout/', logout_user, name='logout'),
	path('finished/<int:pk>', finish_task, name='finished'),
	path('delete/ <int:pk>', delete_task, name='delete'),
]