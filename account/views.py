from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication

from account.serializers import UserSigninSerializer, UserSerializer
from account.models.user import User
from utils import aws

import random


@api_view(["POST"])
def sms_authentication_view(request):
    res = {}
    status_code = status.HTTP_200_OK

    phonenumber = request.GET.get('phonenumber', None)

    if not phonenumber:

        res["phoneNumber"] = "This parameter is required."
        status_code = status.HTTP_400_BAD_REQUEST

    else:

        rnum = random.randint(0, 9)
        list = []

        for i in range(6):
            while rnum in list:
                rnum = random.randint(0, 9)
            list.append(rnum)

        msg = "휴대폰 인증 번호는 \"" + str(''.join(map(str, list))) + "\" 입니다."

        sms_result = aws.send_sms(phoneNumber=phonenumber, message=msg)

        if sms_result["ResponseMetadata"]["HTTPStatusCode"] == 200:
            res = {
                "success": "Successful send sms"
            }

    return Response(res, status_code)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
def account_active_state_view(request, ):
    res = {}
    status_code = status.HTTP_200_OK

    account = User.objects.get(email=request.data["email"])

    if request.data["active"] is False:
        account.is_active = False
        account.save()
        res["success"] = "Successfully account deactive"

    else:
        account.is_active = True
        account.save()
        res["success"] = "Successfully account active"

    return Response(res, status_code)


class SigninView(TokenObtainPairView):
    serializer_class = UserSigninSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
