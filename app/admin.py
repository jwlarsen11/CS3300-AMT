from django.contrib import admin

# Register your models here.
from .models import User
from .models import ForumPost

admin.site.register(ForumPost)