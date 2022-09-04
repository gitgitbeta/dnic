from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Korisnik(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=50)
    surname = models.CharField(max_length=50)

class Lectures(models.Model):
    title=models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    files = models.FileField(upload_to='blog_files/', null=True, blank=True)


class Tests(models.Model):
    title = models.CharField(max_length=50)
    num=models.IntegerField
class Question(models.Model):
    question = models.CharField(max_length=50)
    answer_1 = models.CharField(max_length=50,null=True)
    answer_2 = models.CharField(max_length=50,null=True)
    answer_3 = models.CharField(max_length=50,null=True)
    answer_4 = models.CharField(max_length=50,null=True)
    answer_5 = models.CharField(max_length=50,null=True)
    corectanswer=models.CharField(max_length=50,null=True)
    test=models.ForeignKey(Tests,on_delete=models.CASCADE,null=True)

