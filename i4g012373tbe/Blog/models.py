from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class Title(models.Model):
    title_field = models.CharField(max_length=200)
class Text(models.Model):
    text_field = models.TextField()
class Date(models.Model):
    created_date = models.DateTimeField()
class PublishedDate(models.Model):
    published_date = models.DateTimeField()
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
