import os


def new_user():
    name = input("Welcome to the cinema!\nPlease enter your preferred username: ")
    password = input("\nPlease enter your preferred password: ")
    print("\nThank you for registering, " + name + "!")
    # Write the username and password to a file for future reference
    with open("users.txt", "a") as file:
        file.write(name + "," + password + "\n")
    return name


def login():  # Function to handle the login process
    from Main import display_menu  # Import the display_menu() function from Main.py
    print("\nPlease enter your username:\n")  # Ask the user for their username
    global name  # Declare name as a global variable
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
            return display_menu()
    print("Invalid username or password. Please try again.")
    return login()
