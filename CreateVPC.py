import boto3

#How to create VPC using python! This is really cool... Quicker than the using the AWS Management console
import boto3
client=boto3.client("ec2")
client.create_vpc(CidrBlock='10.0.0.0/16')