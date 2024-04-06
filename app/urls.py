from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forum/', views.forum, name='forum'),
    path('calculator/', views.calculator, name='calculator'),
    path('login/', views.login, name='login'),
]