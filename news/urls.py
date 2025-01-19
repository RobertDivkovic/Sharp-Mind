from . import views
from django.urls import path
from .views import PostList, PostDetail, PostsByAuthor

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),  # Homepage URL
    path('<slug:slug>/', PostDetail.as_view(), name='post-detail'), # Detail view URL
    path('author/<str:username>/', PostsByAuthor.as_view(), name='posts-by-author')
]