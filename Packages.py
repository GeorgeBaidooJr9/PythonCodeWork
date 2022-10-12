import boto3

#A function that prints Hello World
def hello_world():
    print('hello world')
    

#Lab 2- Intro to Boto3

client = boto3.client('translate')

#### Add the new text below this line ####

client = boto3.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='I am learning to code in AWS', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
#### Add the new text below this line ####
    print(response) # this code is inside the function and will print the contents of the variable 'response' 

translate_text() # This line will call our function. Without it, python will not do anything
