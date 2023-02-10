from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import FollowSerializer
from .models import UserFollowing

# Create your views here.
class FollowsView(APIView):

    def post(self, request):
        data = request.data
        data['following_user_id'] = request.user.id
        serializer = FollowSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response ({"msg": "Now you started following",
        "data": serializer.data
        })

    def get(self, request, pk):
        user = UserFollowing.objects.get(id=pk)
        serializer = FollowSerializer(user)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        item = get_object_or_404(UserFollowing, pk=pk)
        item.delete()
        return Response({
            'message': 'You recently unfollow this user.'
        })