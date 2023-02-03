from django.urls import path
from .views import FollowsView

urlpatterns = [
    path('fallo/', FollowsView.as_view(), name='register'),
]