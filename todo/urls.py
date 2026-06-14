from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('complete/<int:id>/',
         views.completeTask,
         name='complete'),

    path('delete/<int:id>/',
         views.deleteTask,
         name='delete'),
]