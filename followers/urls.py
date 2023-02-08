from django.urls import path
from .views import FollowsView

urlpatterns = [
    path('fallo/', FollowsView.as_view(), name='register'),
    path('fallo/<int:pk>', FollowsView.as_view(), name='register'),

]