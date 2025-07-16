from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search_tasks/', views.search_tasks, name='search_tasks'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<str:pk>', views.delete_task, name='delete_task'),
    path('update_task/<str:pk>', views.update_task, name='update_task'),
    path('task_completed/<str:pk>', views.task_completed, name='task_completed'),
    path('view_completed', views.view_completed, name='view_completed'),
]