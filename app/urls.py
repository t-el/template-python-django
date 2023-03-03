from django.contrib import admin
from django.urls import path
from .views import index , AllPostsView,about_site,PostDetailView


app_name = 'app'
urlpatterns = [
    path('', index,name="index"),
    path('about_site/', about_site,name="about_site"),
    path('posts/', AllPostsView.as_view(),name="posts"),
    path('posts/<str:slug>', PostDetailView.as_view(), name='post_detail'),
    #path('create/', creat_post,name="craete_post"),
]
