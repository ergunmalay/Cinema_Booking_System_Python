import os
from modules import seatingManager
import Main

name = ""  # Initialize the name variable to store the user's name

def new_user():
    name = input("Welcome to the cinema!\nPlease enter your preferred username: ")
    password = input("\nPlease enter your preferred password: ")
    print("\nThank you for registering, " + name + "!")
    # Write the username and password to a file for future reference
    with open("users.txt", "a") as file:
        file.write(name + "," + password + "\n")
    return name


def login():  # Function to handle the login process
    print("\nPlease enter your username:\n")  # Ask the user for their username
    global name  # Declare the name variable as global
    name = input()  # Get the user's input for the username
    # Get the user's input for the password
    password = input("\nPlease enter your password:\n")
    # Read the usernames and passwords from the file
    with open("users.txt", "r") as file:  # Open the file in read mode
        users = file.readlines()  # Read all lines from the file
    # Check if the entered username and password match any of the registered users
    for user in users:  # Iterate through each user in the list
        stored_name, stored_password = user.strip().split(
            ",")  # Split the line into username and password
        # Check if the entered username and password match
        if stored_name == name and stored_password == password:
            # Go to display menu
            print("Welcome back, " + name + "!")
            return Main.display_menu()
    print("Invalid username or password. Please try again.")
    return login()

def check_user_file(): # Function to check if the user file exists
    if not os.path.exists("users.txt"): # Check if the file exists
        with open("users.txt", "w") as file: # Open the file in write mode
            file.write("admin,admin\n") # Write the default admin username and password to the file 
    return

def check_seating_file():
    if not os.path.exists("seating.txt"):  # Check if the file exists
        seatingManager.create_seating_file()  # Create the seating arrangement file if it does not exist
    return  # Return if the file does not exist

def check_user_seats_file():
    if not os.path.exists("user_seats.txt"): # Check if the file exists
        with open("user_seats.txt", "w") as file: # Open the file in write mode
            file.write("") # Write an empty string to the file
    return
