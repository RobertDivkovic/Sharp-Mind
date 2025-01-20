from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import (
    PostList,
    PostDetail,
    PostsByAuthor,
    CommentUpdateView,
    CommentDeleteView,
    ProfileView,
    PostVoteView,
    CategoryPostList,
    ContactView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostEditView,
)

urlpatterns = [
    path('', PostList.as_view(), name='home'),  # Homepage URL
    path('contact/', ContactView.as_view(), name='contact'),  # Contact page URL
    path('<slug:slug>/', login_required(PostDetail.as_view()), name='post-detail'),  # Detail view URL restricted to logged-in users
    path('author/<str:username>/', login_required(PostsByAuthor.as_view()), name='posts-by-author'),  # Author posts view restricted to logged-in users
    path('comment/edit/<int:pk>/', CommentUpdateView.as_view(), name='comment-edit'),  # Edit comment URL
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete comment URL
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),  # Profile view URL
    path('post/vote/<int:post_id>/', PostVoteView.as_view(), name='post-vote'),  # Post voting URL
    path('category/<slug:slug>/', CategoryPostList.as_view(), name='category-posts'),  # Filter by category URL
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
