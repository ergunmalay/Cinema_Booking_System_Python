import os

def new_user():
    print("Welcome to the cinema!")
    print("Please enter your preferred username: ")
    name = input()
    print("Please enter your preferred password: ")
    password = input()
    print("Thank you for registering, " + name + "!")
    # Write the username and password to a file for future reference
    with open("users.txt", "a") as file:
        file.write(name + "," + password + "\n")
    return name

def login():
    from Main import display_menu
    print("Please enter your username: ")
    global name
    name = input()
    print("Please enter your password: ")
    password = input()
    # Read the usernames and passwords from the file
    with open("users.txt", "r") as file:
        users = file.readlines()
    # Check if the entered username and password match any of the registered users
    for user in users:
        stored_name, stored_password = user.strip().split(",")
        if stored_name == name and stored_password == password:
            # Go to display menu
            print("Welcome back, " + name + "!")
            return display_menu()
    print("Invalid username or password. Please try again.")
    return login()