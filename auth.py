from os import getenv

import boto3


def get_ec2_client():
    return boto3.client(
        "ec2",
        aws_access_key_id=getenv("aws_access_key_id"),
        aws_secret_access_key=getenv("aws_secret_access_key"),
        aws_session_token=getenv("aws_session_token"),
        region_name=getenv("aws_region_name")
    )
