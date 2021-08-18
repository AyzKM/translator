from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .serializers import UserSerializer, RegistrationSerializer
from .models import User

User = get_user_model()

class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user_object = RegistrationSerializer(data=request.POST)
        if user_object.is_valid():
            password_1 = user_object.validated_data.get('password_1')
            password_2 = user_object.validated_data.get('password_2')
            if password_1 == password_2:
                user = User()
                user.username = user_object.validated_data.get("username")
                user.email = user_object.validated_data.get("email")
                user.set_password(password_1)
                user.save()
                return Response(data=UserSerializer(user).data, status=status.HTTP_201_CREATED)
            else:
                return Response(data={"error":"Passwords does not match"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(data=user_object.errors, status=status.HTTP_400_BAD_REQUEST)

