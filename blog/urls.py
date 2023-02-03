from django.urls import path
from .views import BlogPostView, CommentView, ReplyView

urlpatterns = [
    path('post/', BlogPostView.as_view(), name='blog'),
    path('post/<int:pk>', BlogPostView.as_view(), name='blog'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('comment/<int:pk>', CommentView.as_view(), name='comment_by_id'),
    path('reply/', ReplyView.as_view(), name='reply'),
    path('reply/<int:pk>', ReplyView.as_view(), name='reply'),

]