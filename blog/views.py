from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from.serializers import PostSerializer, CommentSerializer, ReplySerializer
from .models import *
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status

# Create your views here.
class BlogPostView(APIView):
    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = PostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response ({"msg": "Your post is uploaded successfully.",
        "data": serializer.data
        })

    def get(self, request, pk):
        user = Post.objects.get(id=pk)
        serializer = PostSerializer(user)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        item = get_object_or_404(Post, pk=pk)
        item.delete()
        return Response({
            'message': 'Your post Deleted Successfully'
        })

class CommentView(APIView):
    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response ({"msg": "you commented on this post.",
        "data": serializer.data
        })

    def get(self, request, pk):
        user = Comment.objects.get(id=pk)
        serializer = CommentSerializer(user)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        data = Comment.objects.get(id=pk)
        serializer = CommentSerializer(data, data=request.data,)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                serializer.data
            )

    def delete(self, request, pk):
        item = get_object_or_404(Comment, pk=pk)
        item.delete()
        return Response({
            'message': 'Comment Deleted Successfully.'
        })

class ReplyView(APIView):
    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = ReplySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response ({"msg": "you replyed on:",
        "data": serializer.data
        })

    def get(self, request, pk):
        user = Reply.objects.get(id=pk)
        serializer = ReplySerializer(user)
        return Response(serializer.data, status=200)

    def patch(self, request, pk):
        data = Reply.objects.get(id=pk)
        serializer = ReplySerializer(data, data=request.data,)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                serializer.data
            )

    def delete(self, request, pk):
        item = get_object_or_404(Reply, pk=pk)
        item.delete()
        return Response({
            'message': 'Reply Deleted Successfully.'
        })