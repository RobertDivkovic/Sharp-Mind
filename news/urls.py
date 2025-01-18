from . import views
from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),  # Homepage URL
    path('<slug:slug>/', PostDetail.as_view(), name='post-detail'), # Detail view URL
]