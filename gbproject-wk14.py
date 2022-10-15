import boto3

#how to create and launch ec2 using using python boto3
#ec2_resource=boto3.resource("ec2")
#ec2_resource.create_instances(ImageId='ami-026b57f3c383c2eec',
    #InstanceType='t2.micro',
    #MaxCount=3,
    #MinCount=1,)
    

#stop specific ec2 instances for the engineering team using their unique instance ids
ec2 = boto3.resource('ec2')
ec2.Instance('i-08dffa3c0315afc0a').stop()
ec2.Instance('i-0120e9af1a002f15c').stop()
ec2.Instance('i-04ab21ce3d9ef221b').stop()
#["i-08dffa3c0315afc0a"], ["i-0120e9af1a002f15c"], ["i-04ab21ce3d9ef221b"]) 









