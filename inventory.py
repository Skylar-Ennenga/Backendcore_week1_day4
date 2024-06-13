# creating a program to manage items in a list
# declaring the list that will store all of my items
inventory = []

def add_item(inventory):
    item = input("What would you like to add to your inventory? ")
    inventory.append(item)
    print(inventory)

def remove_item(inventory):
    item = input("Which item would you like to remove? ")
    if item in inventory:
        inventory.remove(item)
    else:
        print(f"{item} is not in your inventory...")
    print(inventory)
    

# is responsibly for driving my code
# this is where the while loop will live
# and it will also call all my other functions
def main(inventory):
    print("""
    Please choose from the list below:
          1. add an item to your inventory
          2. remove an item from your inventory
          3. quit
        """)
    while True:
        response = input("What would you like to do? ")
        # conditionals to check the user response and call the necessary functions
        if response == "1":
            add_item(inventory)
        elif response == "2":
            remove_item(inventory)
        elif response == "3":
            print("Be safe out there! Here's what you have")
            print(inventory)
            break
        else: 
            print("Please choose a valid option 1, 2, or 3")

main(inventory)