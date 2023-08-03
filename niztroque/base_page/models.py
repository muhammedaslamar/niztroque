from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,on_delete=models.CASCADE)




    def __str__(self):
        return self.title
class Event(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    location = models.CharField(max_length=100)
    sub_location = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.datetime.now)
    e_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")
    category=models.CharField(max_length=100,default="")
    time=models.CharField(max_length=100,default="")
    amount=models.IntegerField(default=0)
    adress=models.TextField(default="")
    link=models.TextField(default="")

    def __str__(self):
        return self.name

