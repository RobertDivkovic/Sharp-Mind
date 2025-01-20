from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PostList, PostDetail, PostsByAuthor, CommentUpdateView, CommentDeleteView, ProfileView, PostVoteView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),  # Homepage URL
    path('<slug:slug>/', login_required(PostDetail.as_view()), name='post-detail'), # Detail view URL restricted to logged-in users
    path('author/<str:username>/', login_required(PostsByAuthor.as_view()), name='posts-by-author'),  # Author posts view restricted to logged-in users
    path('comment/edit/<int:pk>/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('post/vote/<int:post_id>/', PostVoteView.as_view(), name='post-vote'),
]