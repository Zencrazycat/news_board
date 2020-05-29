from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField(max_length=256)
    creation_date = models.DateField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    author = models.CharField(max_length=128)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    author = models.CharField(max_length=128)
    content = models.TextField()
    creation_date = models.DateField(default=timezone.now)
