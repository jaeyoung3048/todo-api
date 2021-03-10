from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import mixins, generics

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSigninSerializer, UserSerializer
from .models import User


class SigninView(TokenObtainPairView):
    serializer_class = UserSigninSerializer


class SignupView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


