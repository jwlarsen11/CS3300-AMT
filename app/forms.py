from django.forms import HiddenInput, ModelForm
from django.forms import forms
from .models import User, ForumPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = ForumPost
        fields =['title', 'body', 'public']

class DeletePostForm(forms.Form):
    pass

class UserForm(ModelForm):
    class Meta:
        Model = User