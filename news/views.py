from django.shortcuts import render, get_object_or_404, redirect 
from django.views import generic
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "news/index.html"
    context_object_name = "posts"
    paginate_by = 5

class PostDetail(FormMixin, generic.DetailView):
    model = Post
    template_name = "news/post_detail.html"  # Path to the template for individual posts
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()  # Add the comment form to the context
        context['comments'] = Comment.objects.filter(post=self.object, approved=True)  # Add approved comments
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object  # Associate comment with the post
            comment.author = request.user.username  # Use the logged-in user's username
            comment.save()
            messages.success(request, "Your comment has been submitted successfully!")
            return redirect('post-detail', slug=self.object.slug)  # Redirect to the same post
        return self.form_invalid(form)

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
