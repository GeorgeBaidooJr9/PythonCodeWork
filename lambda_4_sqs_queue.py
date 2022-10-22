import json
import boto3

from datetime import datetime

def lambda_handler(event, context):
   
    # datetime object containing current date and time
    now = datetime.now()
 

    # date and time shown in old school fashion. 
    todays_date = now.strftime("%d/%m/%Y %H:%M:%S")
    

    sqs = boto3.client('sqs')
    
    sqs.send_message(QueueUrl="https://sqs.us-east-1.amazonaws.com/374711145665/boba_queue",MessageBody=todays_date)
  
    return {
        'statusCode': 200,
        'body': json.dumps('Successs... Few more steps though')
    }

