from django.shortcuts import render, get_object_or_404
from django.views import generic
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