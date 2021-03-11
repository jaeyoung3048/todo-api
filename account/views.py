from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSigninSerializer, UserSerializer
from .models import User
from utils import aws

import random


@api_view(["POST"])
def sms_authentication(request, ):

    res = {}
    status_code = status.HTTP_200_OK

    if "phoneNumber" not in request.data:

        res["phoneNumber"] = "This field is required."
        status_code = status.HTTP_400_BAD_REQUEST

    else:
        phoneNumber = request.data["phoneNumber"]

        rnum = random.randint(0, 9)
        list = []

        for i in range(6):
            while rnum in list:
                rnum = random.randint(0, 9)  # 중복되면 다시 뽑기
            list.append(rnum)

        msg = "휴대폰 인증 번호는 \""+str(''.join(map(str, list)))+"\" 입니다."

        sms_result = aws.send_sms(phoneNumber=phoneNumber, message=msg)

        if sms_result["ResponseMetadata"]["HTTPStatusCode"] == 200:
            res={
                "success": "Successful send sms"
            }

    return Response(res, status_code)


class SigninView(TokenObtainPairView):
    serializer_class = UserSigninSerializer


class SignupView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

