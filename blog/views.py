from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView, DetailView

posts = Post.objects.all()

def home(request):
    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-publish_date']

class PostDetailView(DetailView):
    model = Post

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'blog/about.html', context)
