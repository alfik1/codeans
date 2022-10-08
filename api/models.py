from django.db import models
from django.contrib.auth.models import User

class Questions(models.Model):
    qs_desc=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images', null=True)
    created_on=models.DateTimeField(auto_now_add=True)

class Answers(models.Model):
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='an_user')
    upvote=models.ManyToManyField(User)
    posted_date=models.DateTimeField(auto_now_add=True)
