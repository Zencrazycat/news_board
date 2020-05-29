from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=128)
    link = models.URLField(max_length=256)
    creation_date = models.DateField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    author = models.CharField(max_length=128)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.title}. (author: {self.author}). ({self.creation_date})'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='posts')
    author = models.CharField(max_length=128)
    content = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
