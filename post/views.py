from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    
    # context name in normal equal ['object_list', 'modelname_list']
    
    model = Post

    context_object_name = 'all_posts'
    ordering = ['-created_at']
    # queryset = Post.objects.filter(active=True)
    # template_name = 'post/test.html'
    
    def get_queryset(self):
        return Post.objects.filter(active=True)
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["my_name"] = 'Ahmed'
        return context
    




class PostDetail(DetailView):
    model = Post

class PostUpdate(UpdateView):
    pass

class PostDelete(DeleteView):
    pass

class PostCreate(CreateView):
    pass

