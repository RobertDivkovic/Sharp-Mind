from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import PostList, PostDetail, PostsByAuthor

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),  # Homepage URL
    path('<slug:slug>/', login_required(PostDetail.as_view()), name='post-detail'), # Detail view URL restricted to logged-in users
    path('author/<str:username>/', login_required(PostsByAuthor.as_view()), name='posts-by-author'),  # Author posts view restricted to logged-in users
]