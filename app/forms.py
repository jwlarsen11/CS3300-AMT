from django.forms import HiddenInput, ModelForm
from django.forms import forms
from .models import Member, ForumPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(ModelForm):
    class Meta:
        model = ForumPost
        fields =['title', 'body', 'public', 'upload_image']

class DeletePostForm(forms.Form):
    pass

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude =['user']
