from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import PostForm, DeletePostForm, UserForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def calculator(request):
    return render(request, 'app/calculator.html')

def forum(request):
    posts = ForumPost.objects.filter(public=True)
    return render(request, 'app/forum.html', {'posts': posts})

def view_post(request, post_id):
    post = get_object_or_404(ForumPost, pk=post_id)
    return render(request, 'app/post_detail.html', {'post':post})

def update_post(request, post_id):
    post = get_object_or_404(ForumPost, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('view-post', post_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'app/update_post.html', {'form': form, 'post': post})

def delete_post(request, post_id):
    post = ForumPost.objects.get(pk= post_id)
    form = DeletePostForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        post.delete()
        return redirect('/forum')
    return render(request, 'app/delete_post.html', {'form': form, 'post': post})

def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        post_data = request.POST.copy()
        form = PostForm(post_data)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/forum')
    
    context= {'form': form}
    return render(request, 'app/create_post.html', context)



class UserListView(generic.ListView):
    model = User

class UserDetailView(generic.DetailView):
    model = User

class PostDetailView(generic.DetailView):
    model = ForumPost