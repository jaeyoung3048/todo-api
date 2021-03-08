from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from account.models import User


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSigninSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


'''class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.name'''