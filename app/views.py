from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from .models import *
from .forms import PostForm, DeletePostForm, CreateUserForm, MemberForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.models import Group
from .decorators import allowed_users

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def login(request):
   return render(request, 'app/login.html')

@login_required(login_url='login')
def logout(request):
    return render(request, 'registration/logout.html', {})

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Members_Role')
            user.groups.add(group)
            member = Member.objects.create(user=user,)
            member.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        
    context ={'form':form}
    return render(request, 'registration/register.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['members_role'])
def userPage(request):
    member = request.user.member
    form = MemberForm(instance = member)
    print('member', member)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'app/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['members_role'])
def calculator(request):
    return render(request, 'app/calculator.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['members_role'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['members_role'])
def delete_post(request, post_id):
    post = ForumPost.objects.get(pk= post_id)
    form = DeletePostForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        post.delete()
        return redirect('/forum')
    return render(request, 'app/delete_post.html', {'form': form, 'post': post})

@login_required(login_url='login')
@allowed_users(allowed_roles=['members_role'])
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



class UserListView(LoginRequiredMixin, generic.ListView):
    model = User

class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User

class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = ForumPost