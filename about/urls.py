from django.urls import path
from .views import AboutPageView, CollaborationRequestView

urlpatterns = [
    path('', AboutPageView.as_view(), name='about'),
    path('collaboration/', CollaborationRequestView.as_view(), name='collaboration'),
]