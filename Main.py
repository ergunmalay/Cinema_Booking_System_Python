import os

# Function to display the main menu options to the user


def display_menu():
    from bookingManager import book_seat, cancel_booking, check_bookings
    from seatingManager import display_seating
    option = input(
        "Please select an option:\n1. Display seating arrangement\n2. Book a seat\n3. Cancel booking\n4. Check bookings\n5. Exit\n (1/2/3/4/5)\n")
    if option == "1":
        return display_seating()
    elif option == "2":
        return book_seat()
    elif option == "3":
        return cancel_booking()
    elif option == "4":
        return check_bookings()
    elif option == "5":
        print("Thank you for using the cinema booking system. Goodbye!")
        exit()
    else:
        print("Invalid option. Please try again.")
        return display_menu()


# Function to handle the flow for a normal user
def normal_user():  # Function to handle the flow for a normal user
    # Import new_user() and login() functions from userManager.py
    from userManager import new_user, login
    # Ask the user if they are a new user
    response = input("\nAre you a new user? (Y/N)\n\n")
    if response.lower() == "y":  # If the user is a new user
        new_user()  # Call the new_user() function
        display_menu()  # Call display_menu() after new_user()
    elif response.lower() == "n":  # If the user is not a new user
        login()  # Call the login() function
        display_menu()  # Call display_menu() after login()
    else:
        print("\nInvalid option. Please try again.")
        normal_user()

# Function to handle admin login


def admin_login():
    from adminUser import admin_display_menu
    # Ask the admin for the password
    password = input("\nWelcome, admin!\nPlease enter the admin password:\n\n")
    if password == "admin":  # If the password is correct
        print("\nAccess granted!")  # Print "Access granted!"
        admin_display_menu()  # Call the admin_display_menu() function
    else:
        print("\nIncorrect password. Access denied.")
        admin_login()

# Main function to start the program


def main():
    # Import is_file_empty() function from seatingManager.py
    from seatingManager import is_file_empty
    is_file_empty()  # Check if the file is empty
    user_type = input(
        "Welcome to the cinema booking system! Are you a normal user or an admin? (normal/admin)\n\n")
    if user_type == "normal":  # If the user is a normal user
        normal_user()  # Call the normal_user() function
    elif user_type == "admin":  # If the user is an admin
        admin_login()  # Call the admin_login() function
    else:
        print("Invalid option. Please try again.")
        main()


# Entry point of the program
if __name__ == "__main__":
    main()
