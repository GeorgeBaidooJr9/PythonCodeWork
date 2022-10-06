#My first python code project with aws
#Created a list of aws services

a = ['aws ec2', 'dynamodb', 's3', 'lambda']
print(a, "My list of AWS services!")

#adding 2 more services to the list using "append" function and printing the list with new changes
a.append('sdk')
a.append('code9')
print(a, "This list contains two added services!")

#deleting 2 specific items from the list and printing the new list
a.remove('s3')
a.remove('lambda')
print(a, "New updated list, with two services deleted!")
