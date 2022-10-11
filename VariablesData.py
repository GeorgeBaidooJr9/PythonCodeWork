first_name = "Monty"
#first_name is the variable. Monty is the value assigned.
last_name = "Python"
print(first_name + " " + last_name)

first_name = "John"
surname = "Doe"
print("My first name is {}. My family name is {}". format(first_name, surname))

#NUMBERS
my_int = 50
sentence = "The total comes to: "
print(sentence + str(my_int)) 

#Dictionary time. A dictionary is a way of storing related information in key-value pairs. 
#Creating, Reading, Updating and Deleting values in a dictionary 
#Dictionaries can be changed after you create them. 
cool_user= ["family_name"]
print(cool_user)
{'first_name': 'Ada'}

#Creating, Reading, Updating and Deleting elements in a list
fruit = ["apples", "oranges", "bananas"]
print(fruit[1])

print(fruit[-1])
print(fruit[-2])

#Updating list, add, update, and deleting items in a list
fruit.append("kiwi")
print(fruit)
['apples', 'oranges', 'bananas', 'kiwi']

#Determing Type (This code results in an error)
my_variable = "A string"
print(type(my_variable))
