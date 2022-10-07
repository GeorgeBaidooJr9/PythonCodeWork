import random 

n = random.randint(0,10)

print(n)

if(n > 5):
    print("big number")
elif(n < 5):
    print("Small number")
elif(n ==5):
    print("equals 5")
    
numbers = [random.randint(0,10) for i in range(10)]

print(numbers)

if(threshold in numbers):
    print(str(threshold) + " is in numbers")
    