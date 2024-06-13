# 1. The Calculator App

# Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation, with parameters for two numbers to be used in the operation. 
# Task 2: Implement user input to receive numbers and an operation choice, their response for operation should call the associated function.

# if operation == "add":
#     add(num_1, num_2)

def addition(num1, num2):
    add_output = (num1 + num2)
    print(f"That eqauls {add_output}")

def subtraction(num1, num2):
    sub_output = (num1 - num2)
    print(f"That eqauls {sub_output}")
    
def multiplication(num1, num2):
    mult_output = (num1 * num2)
    print(f"That eqauls {mult_output}")
    

def division(num1, num2):
    div_output = (num1 / num2)
    print(f"That eqauls {div_output}")
    
def main():
    print("""
    Please choose from the list below:
          1. Add
          2. Subtract
          3. Multiply
          4. Divide
        """)
    while True:
        response = input("What would you like to do? ")
        # conditionals to check the user response and call the necessary functions
        if response == "1":
            num1 = int(input("Tell me the first number you would like to use: "))
            num2 = int(input("Tell me the second number you would like to use: "))
            addition(num1, num2)
            break
        elif response == "2":
            num1 = int(input("Tell me the first number you would like to use: "))
            num2 = int(input("Tell me the second number you would like to use: "))
            subtraction(num1, num2)
            break
        elif response == "3":
            num1 = int(input("Tell me the first number you would like to use: "))
            num2 = int(input("Tell me the second number you would like to use: "))
            multiplication(num1, num2)
            break
        elif response == "4":
            num1 = int(input("Tell me the first number you would like to use: "))
            num2 = int(input("Tell me the second number you would like to use: "))
            division(num1, num2)
            break
        else: 
            print("Please choose a valid option 1, 2, 3, or 4")


main()




# 2. The Shopping List Maker

# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list, make sure you ask the user what they would like to add (reminder: ensure the function has a parameter to receive the list).
# Task 2: Include a feature to remove items from the list. 
# Task 3: Add a function that prints out the entire list.