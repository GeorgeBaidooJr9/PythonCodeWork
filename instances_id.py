import boto3

#how to create and launch ec2 using using python boto3
ec2_resource=boto3.resource("ec2")
client=boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
 for printout in pythonins['Instances']:
  for printname in printout['Tags']:
   print(printout['InstanceId'])
   print(printout['InstanceType'])
   print(printout['State']['Name'])
   print(printname['Value'])
    


#ec2_resource.create_instances(ImageId='ami-026b57f3c383c2eec',
    #InstanceType='t2.micro',
    #MaxCount=2,
    #MinCount=1,)
