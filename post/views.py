from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class PostUpdate(UpdateView):
    pass

class PostDelete(DeleteView):
    pass

class PostCreate(CreateView):
    pass

