from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('posts/<slug:slug>/', views.group_posts, name='group_posts'),
    path('group/<slug>/', views.group_list, name='group_list'),
]
