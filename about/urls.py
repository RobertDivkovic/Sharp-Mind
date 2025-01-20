from django.urls import path
from .views import (
    AboutPageView,
    CollaborationRequestView,
    CollaborationRequestUpdateView,
    CollaborationRequestDeleteView,
)

urlpatterns = [
    path('', AboutPageView.as_view(), name='about'),
    path('collaboration/', CollaborationRequestView.as_view(), name='collaboration'),
    path('collaboration/edit/<int:pk>/', CollaborationRequestUpdateView.as_view(), name='collaboration-edit'),
    path('collaboration/delete/<int:pk>/', CollaborationRequestDeleteView.as_view(), name='collaboration-delete'),
]