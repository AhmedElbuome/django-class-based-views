from . import views
from django.contrib import admin
from django.urls import path

app_name = 'post'

urlpatterns = [
    path("", views.PostList.as_view(), name = 'post_list'),
    path("<int:pk>/", views.PostDetail.as_view(), name = 'post_detail'),
    
]