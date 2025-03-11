from django.urls import path
from . import views

urlpatterns = [
    path('ping', views.Ping.as_view()),
    path('signup', views.SignUp.as_view()),
    path('createtask', views.CreateTask.as_view()),
    path('gettasks', views.GetTasks.as_view()),
    path('login', views.LogIn.as_view()),
]