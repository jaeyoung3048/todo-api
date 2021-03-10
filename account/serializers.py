from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from account.models import User


class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )

        return user

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name", "is_staff", "is_admin"]


class UserSigninSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token["permission"] = {
            "is_staff": user.is_staff,
            "is_admin": user.is_admin,
            "is_superuser": user.is_superuser,
        }

        usermodels = User.objects.get(email=user.email)
        usermodels.refresh_token = token
        usermodels.save()

        return token