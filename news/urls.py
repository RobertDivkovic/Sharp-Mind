from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import (
    PostList,
    PostDetail,
    PostsByAuthor,
    CommentUpdateView,
    CommentDeleteView,
    profile_view,  # Ensure profile_view is correctly imported
    PostVoteView,
    CategoryPostList,
    ContactView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostList.as_view(), name='home'),  # Homepage URL

    path('contact/', ContactView.as_view(), name='contact'),

    path('<slug:slug>/', login_required(PostDetail.as_view()),
         name='post-detail'),

    path('author/<str:username>/', login_required(PostsByAuthor.as_view()),
         name='posts-by-author'),

    path('comment/edit/<int:pk>/', CommentUpdateView.as_view(),
         name='comment-edit'),  # Edit comment URL

    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(),
         name='comment-delete'),
    path('profile/<str:username>/', profile_view, name='profile'),
    path('post/vote/<int:post_id>/', PostVoteView.as_view(), name='post-vote'),
    path('category/<slug:slug>/', CategoryPostList.as_view(),
         name='category-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(),
         name='post-delete'),
]
