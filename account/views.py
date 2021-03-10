from rest_framework.decorators import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import MyTokenObtainPairSerializer
from .models import User


class SigninView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

