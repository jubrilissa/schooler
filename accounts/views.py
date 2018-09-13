from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import UserSerializer


class UserView(APIView):
    def get(self, request, format=None):
        students = User.objects.all()
        serializer = UserSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({"message": "User successfully created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenView(ObtainAuthToken):
    def post(self, request):
        response = super(TokenView, self).post(request)
        return response
