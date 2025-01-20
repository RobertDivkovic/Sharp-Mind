from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.utils.timezone import now  # Corrected timezone import
from .models import Post, Comment, Vote
from .forms import CommentForm
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Post List View
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "news/index.html"
    context_object_name = "posts"
    paginate_by = 5

# Post Detail View with Comment Form
class PostDetail(FormMixin, generic.DetailView):
    model = Post
    template_name = "news/post_detail.html"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        # Approved comments visible to all
        context['comments'] = Comment.objects.filter(post=self.object, approved=True)
        # Pending comments visible only to the logged-in user
        if self.request.user.is_authenticated:
            context['pending_comments'] = Comment.objects.filter(
                post=self.object, approved=False, user=self.request.user
            )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object  # Associate comment with the post
            comment.author = request.user.username  # Set the logged-in user's username
            comment.user = request.user  # Set the user field to the logged-in user
            comment.save()
        messages.success(request, "Your comment has been submitted successfully!")
        return redirect('post-detail', slug=self.object.slug)  # Redirect to the same post
        return self.form_invalid(form)

# Profile View
class ProfileView(generic.TemplateView):
    template_name = "news/profile.html"

    def get_context_data(self, **kwargs):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        context = super().get_context_data(**kwargs)
        context['profile_user'] = user
        context['user_posts'] = Post.objects.filter(author=user)
        context['user_comments'] = Comment.objects.filter(user=user)
        context['user_votes'] = Vote.objects.filter(user=user)
        context['upvoted_posts'] = Post.objects.filter(upvotes=user)
        context['downvoted_posts'] = Post.objects.filter(downvotes=user)
        return context

# Posts By Author View
class PostsByAuthor(generic.ListView):
    model = Post
    template_name = "news/posts_by_author.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        username = self.kwargs['username']
        return Post.objects.filter(author__username=username, status=1).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = User.objects.get(username=self.kwargs['username'])
        return context

# Post Update View
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'status']
    template_name = 'news/post_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "The post has been updated successfully!")
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Post Delete View
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'news/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Comment Update View
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['body']
    template_name = 'news/comment_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.updated_on = now()  # Update the timestamp when saving
        messages.success(self.request, "Your comment has been updated successfully!")
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user

# Comment Delete View
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'news/comment_confirm_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.user

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class PostVoteView(LoginRequiredMixin, View):
    @method_decorator(csrf_exempt)  # Exempt CSRF for now if necessary
    def post(self, request, *args, **kwargs):
        try:
            post = get_object_or_404(Post, id=self.kwargs['post_id'])
            data = json.loads(request.body)  # Parse JSON request body
            vote_type = data.get('vote_type')  # Extract vote type

            if vote_type == 'upvote':
                # Handle upvote logic
                if post.downvotes.filter(id=request.user.id).exists():
                    post.downvotes.remove(request.user)
                post.upvotes.add(request.user)
            elif vote_type == 'downvote':
                # Handle downvote logic
                if post.upvotes.filter(id=request.user.id).exists():
                    post.upvotes.remove(request.user)
                post.downvotes.add(request.user)
            else:
                return JsonResponse({'error': 'Invalid vote type'}, status=400)

            # Return updated vote counts
            return JsonResponse({
                'total_upvotes': post.upvotes.count(),
                'total_downvotes': post.downvotes.count(),
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
