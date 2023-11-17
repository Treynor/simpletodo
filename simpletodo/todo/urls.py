from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name="task_list"),
    path('new/', views.task_create, name="task_new"),
    path('<int:id>/edit/', views.task_update, name="task_edit"),
    path('<int:id>/delete/', views.task_delete, name="task_delete"),
]
