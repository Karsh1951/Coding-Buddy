from django.db import models
#importing users
from django.contrib.auth.models import User

# Create your models here.
#creating the first table for room
#creating topic
class User():
    name = models.CharField(max_length=200, null= True)
    email = models.EmailField(unique=True, null=True,)
    bio = models.Model.CharField(null=True)
    avatar = models.ImageField(null=True,default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name  
    
    
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    #participants
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering =['-updated', '-created']
    #auto now add only records the value once ,auto now records each time an update occurs
    def __str__(self):
        return self.name
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[0:50]
        
    
    
    
         
    
    
    
    
    
    
    