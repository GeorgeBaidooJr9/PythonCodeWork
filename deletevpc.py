import boto3

#Removing vpc via python boto3

client=boto3.client("ec2")
response = client.delete_vpc(
   VpcId='vpc-006e28dc07e3229bc'
   
)