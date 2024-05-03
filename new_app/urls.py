from django.urls import path

from new_app import views

urlpatterns = [
path('',views.index,name='index2'),
path('index',views.index,name='index'),
path('home',views.home,name='home'),
path('todo',views.todo,name='todo'),
path('todo2',views.views_todo,name='views_todo'),
path("delete/<int:id>/",views.delete,name='delete'),
path("update/<int:id>/",views.update,name='update')
]


