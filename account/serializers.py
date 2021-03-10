from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from account.models import User


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserSigninSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token["permission"] = {
            "is_staff": user.is_staff,
            "is_admin": user.is_admin,
            "is_superuser": user.is_superuser,
        }

        usermodels = User.object.get(email=user.email)
        usermodels.refresh_token = token
        usermodels.save()

        return token