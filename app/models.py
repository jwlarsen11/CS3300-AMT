from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import datetime



class Member(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

class ForumPost(models.Model):
    #op = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='posts')
    date = models.DateTimeField(default=datetime.datetime.now())
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=1000)
    public = models.BooleanField(default=False)
    upload_image = models.ImageField(null=True, blank=True, upload_to="images/")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("view-post", args=[str(self.id)])
    
class ForumComment(models.Model):
    #op = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='commenter')
    #post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, default=None, related_name='comments')
    text = models.CharField(max_length=200)