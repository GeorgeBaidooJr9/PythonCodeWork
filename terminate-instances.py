import boto3
client = boto3.client('ec2')

#terminating specific ec2 instances using their instance id
Instances = client.terminate_instances(InstanceIds=['i-09da7405b89a1c730', 'i-068b4ec99d3c0f0ca'])
print(Instances)