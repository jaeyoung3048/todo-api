import boto3
from utils.secrets import *

client = boto3.client(
    "sns",
    aws_access_key_id= get_secret("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key= get_secret("AWS_SECRET_ACCESS_KEY"),
    region_name="us-east-1"
)


def send_sms(phoneNumber, Message, aws=client):
    res = aws.publish(
        PhoneNumber= "+82"+phoneNumber,
        Message=Message
    )

    return res
