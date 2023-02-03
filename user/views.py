from user.serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class RegisterView(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response ({"msg": serializer.data})