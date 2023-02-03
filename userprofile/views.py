from django.shortcuts import render
from .serializers import ProfileSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .paginations import CustomPagination
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Profile
# Create your views here.

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated,]

    serializer_class = ProfileSerializer
    def post(self, request):
        data = request.data
        data["users"] = request.user.id
        serializer = ProfileSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"profile": serializer.data})


    def get(self, request, pk=None):
        if pk is not None:
            user = Profile.objects.get(id=pk)
            serializer = ProfileSerializer(user)
        else:
            user = Profile.objects.all()
            serializer = ProfileSerializer(user, many=True)
        return Response(serializer.data, status=200)
        
    def patch(self, request, pk):
        data = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(data, data=request.data,)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                serializer.data
            )

    def delete(self, request, pk):
        item = get_object_or_404(Profile, pk=pk)
        item.delete()
        return Response({
            'message': 'Task Deleted Successfully'
        })


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_record(self, request, pk):
        self.pagination_class = CustomPagination
        queryset = self.filter_queryset(self.queryset.filter(course=pk))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data) 