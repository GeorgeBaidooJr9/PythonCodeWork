import random 
import string


#project will consist of the user input of how many instances they want, with corresponding unique names 
#2 allow the users to input the name of their department that is used in the unique name
#3 Generate random characters and numbers that will be included in the unique name 
#

#departments that user can choose from. Upon selection the user will input their department of choice!
department_info = set(["Marketing", "Accouting", "FinOps"])
print(department_info)
department_choice = input("Choose your desired department:" )


#Prompts user to type the word YES to have their EC2 instances assigned a uniquely generated name.
ec2_instances = input("Type YES so that your EC2 instances will be assigned unique generated names: ")
if ec2_instances == "YES":
    print("Ok, next step forward")
   
#User is prompt to enter the desired number of EC2 instances they need!
ec2_instances = input("How many EC2 instances will you need?: ")
ec2_instances = int(ec2_instances)

for i in range(ec2_instances):

 x = random.randint(0, 100)
 a = random.randint(0, 1000)
print("Generated Name's for Department: ")
print(department_choice, '1', str(x))
print(department_choice, '2', str(a))





