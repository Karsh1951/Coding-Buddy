from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    #passing in the id into the url(pk stands for primary key)
    path('room/<str:pk>/',views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),  
]
