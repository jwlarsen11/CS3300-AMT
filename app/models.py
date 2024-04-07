from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse("user-detail", args=[str(self.id)])
    
class ForumPost(models.Model):
    #op = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='posts')
    date = models.DateTimeField(default=datetime.datetime.now())
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=1000)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("view-post", args=[str(self.id)])
    
class ForumComment(models.Model):
    #op = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='commenter')
    #post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, default=None, related_name='comments')
    text = models.CharField(max_length=200)