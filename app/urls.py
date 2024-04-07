from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calculator/', views.calculator, name='calculator'),
    path('login/', views.login, name='login'),

    path('users/', views.UserListView.as_view(), name='users'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),

    path('forum/', views.forum, name='forum'),
    path('forum/create_post', views.create_post, name='create-post'),
    path('forum/<int:post_id>', views.view_post, name='view-post'),
    path('forum/<int:post_id>/update_post', views.update_post, name='update-post'),
    path('forum/<int:post_id>/delete_post', views.delete_post, name='delete-post'),
    
]