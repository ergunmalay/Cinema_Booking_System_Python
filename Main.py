import os
from modules import bookingManager, seatingManager, userManager, adminUser

# Function to display the main menu options to the user
def display_menu():
    option = input(
        "Please select an option:\n1. Display seating arrangement\n2. Book a seat\n3. Cancel booking\n4. Check bookings\n5. Exit\n (1/2/3/4/5)\n")
    if option == "1":
        return seatingManager.display_seating()
    elif option == "2":
        return bookingManager.book_seat()
    elif option == "3":
        return bookingManager.cancel_booking()
    elif option == "4":
        return bookingManager.check_bookings()
    elif option == "5":
        print("Thank you for using the cinema booking system. Goodbye!")
        exit()
    else:
        print("Invalid option. Please try again.")
        return display_menu()


# Function to handle the flow for a normal user
def normal_user():  # Function to handle the flow for a normal user
    # Import new_user() and login() functions from userManager.py
    # Ask the user if they are a new user
    response = input("\nAre you a new user? (Y/N)\n\n")
    if response.lower() == "y":  # If the user is a new user
        userManager.new_user()  # Call the new_user() function
        display_menu()  # Call display_menu() after new_user()
    elif response.lower() == "n":  # If the user is not a new user
        userManager.login()  # Call the login() function
        display_menu()  # Call display_menu() after login()
    else:
        print("\nInvalid option. Please try again.")
        normal_user()

# Function to handle admin login


def admin_login():
    # Ask the admin for the password
    password = input("\nWelcome, admin!\nPlease enter the admin password:\n\n")
    if password == "admin":  # If the password is correct
        print("\nAccess granted!")  # Print "Access granted!"
        adminUser.admin_display_menu()  # Call the admin_display_menu() function
    else:
        print("\nIncorrect password. Access denied.")
        admin_login()

# Main function to start the program


def main():
    # Import is_file_empty() function from seatingManager.py
    seatingManager.is_file_empty()  # Check if the file is empty

    userManager.check_user_file()  # Check if the user file exists

    userManager.check_user_seats_file()  # Check if the user seats file exists

    user_type = input(
        "Welcome to the cinema booking system! Are you a normal user or an admin?\n1. Normal\n2. Admin \n\n")
    if user_type == "1":  # If the user is a normal user
        normal_user()  # Call the normal_user() function
    elif user_type == "2":  # If the user is an admin
        admin_login()  # Call the admin_login() function
    else:
        print("Invalid option. Please try again.")
        main()


# Entry point of the program
if __name__ == "__main__":
    main()