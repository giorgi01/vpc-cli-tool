import argparse
import boto3
from botocore.exceptions import ClientError
from auth import get_ec2_client


def create_vpc(client, name):
    try:
        vpc = client.create_vpc(CidrBlock='10.0.0.0/16')
        vpc.create_tags(Tags=[{'Key': 'Name', 'Value': name}])
        return vpc
    except ClientError as e:
        print(e.response)
        return None


def create_igw(client, name):
    try:
        igw = client.create_internet_gateway()
        igw.create_tags(Tags=[{'Key': 'Name', 'Value': f'{name}-IGW'}])
        return igw
    except ClientError as e:
        print(e.response)
        return None


def attach_igw_to_vpc(client, igw_id, vpc_id):
    try:
        client.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
        return True
    except ClientError:
        return False


def main():
    parser = argparse.ArgumentParser(
        description="CLI program that helps with VPC",
        prog='main.py',
        epilog='DEMO APP'
    )

    parser.add_argument('cmd', help='Command', choices=['vpc', 'igw', 'attach'])
    parser.add_argument('--vpc_name', type=str)
    parser.add_argument('--igw_name', type=str)
    parser.add_argument('--vpc_id', type=str)
    parser.add_argument('--igw_id', type=str)

    args = parser.parse_args()

    ec2_client = get_ec2_client()

    if args.cmd == 'vpc':
        vpc = create_vpc(ec2_client, args.vpc_name)
        if vpc is not None:
            print(f"Created VPC: {vpc.id}, {vpc.name}")
    elif args.cmd == 'igw':
        igw = create_igw(ec2_client, args.igw_name)
        if igw is not None:
            print(f"Created IGW: {igw.id}, {igw.name}")
    elif args.cmd == 'attach':
        if attach_igw_to_vpc(ec2_client, args.igw_id, args.vpc_id):
            print("Successfully attached")


if __name__ == '__main__':
    main()
