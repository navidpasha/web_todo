from django.contrib import admin
from django.urls import path,reverse,re_path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete/<path:name>/', views.delete_todo, name='delete'),
    path('update/<str:name>/', views.update, name='update'),
]

