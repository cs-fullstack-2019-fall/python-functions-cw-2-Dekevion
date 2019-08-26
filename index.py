#Problem 1:

# Create a function that will ask the user for a number. 
# Use the function to get two numbers from the user, 
# then pass the two numbers to a function. Add, subtract, multiple, and divide the numbers.

def twoNum():
    num1 = int(input('enter number'))
    num2 = int(input('enter number'))
    add(num1, num2)


def add(num1, num2):
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)
    
twoNum()