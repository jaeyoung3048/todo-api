from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer

from account.models.user import User
from account.models.user_profile import Profile


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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
        write_only_fields = ["password"]


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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["email", "first_name", "last_name", "photo"]
        read_only_fields = ["email"]