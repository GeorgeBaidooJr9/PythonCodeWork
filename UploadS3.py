import boto3
import os
import glob

#how to upload single file
s3_resource=boto3.client("s3")
s3_resource.upload_file(
Filename="test1.png",
Bucket="totaltechnology22",
Key="test.png")
    
#how to upload multiple files
cwd=os.getcwd()
cwd=cwd+"/upload/"
files=glob.glob(cwd+"*.png") 