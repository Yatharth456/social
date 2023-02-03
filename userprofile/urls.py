from django.urls import path
from .views import ProfileView, ProfileViewSet


urlpatterns = [
    path('post/', ProfileView.as_view(), name='profile'),
    path('post/<int:pk>', ProfileView.as_view(), name='get_by_id'),
    path('page/', ProfileViewSet.as_view({'get': 'list'}), name='pagination'),

]