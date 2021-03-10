from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSigninSerializer, UserSerializer
from .models import User
from utils import aws


@api_view(["POST"])
def sms_authentication(request, ):

    res = {}
    status_code = status.HTTP_200_OK

    if "phoneNumber" not in request.data:

        res["phoneNumber"] = "This field is required."
        status_code = status.HTTP_400_BAD_REQUEST

    elif "message" not in request.data:

        res["message"] = "This field is required."
        status_code = status.HTTP_400_BAD_REQUEST

    else:
        phoneNumber = request.data["phoneNumber"]
        message = request.data["message"]

        sms_result = aws.send_sms(phoneNumber, message)

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


@api_view(["GET"])
def testview(request):

    phoneNumber = request.data

    return Response(str(type(phoneNumber)), status.HTTP_200_OK)