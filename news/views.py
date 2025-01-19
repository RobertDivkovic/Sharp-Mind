from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "news/index.html"
    context_object_name = "posts"
    paginate_by = 5

class PostDetail(generic.DetailView):
    model = Post
    template_name = "news/post_detail.html" # Path to the template for individual posts

class PostsByAuthor(generic.ListView):
    model = Post
    template_name = "news/posts_by_author.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        username = self.kwargs['username']  # Get the 'username' from the URL
        return Post.objects.filter(author__username=username, status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = User.objects.get(username=self.kwargs['username'])
        return context