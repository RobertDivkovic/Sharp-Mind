from django.urls import path
from .views import (
    AboutPageView,
    CollaborationRequestView,
    CollaborationRequestUpdateView,
    CollaborationRequestDeleteView,
)

urlpatterns = [
    path('', AboutPageView.as_view(), name='about'),
    path('collaboration-request/', CollaborationRequestView.as_view(), name='collaboration_request'),
    path('collaboration-request/<int:pk>/update/', CollaborationRequestUpdateView.as_view(), name='collaboration_request_update'),
    path('collaboration-request/<int:pk>/delete/', CollaborationRequestDeleteView.as_view(), name='collaboration_request_delete'),
]