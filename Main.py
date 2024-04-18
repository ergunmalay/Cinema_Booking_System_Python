import os

# Function to display the main menu options to the user
def display_menu():
    from bookingManager import  book_seat, cancel_booking, check_bookings
    from seatingManager import display_seating

    print("Please select an option:")
    print("1. View seating arrangement")
    print("2. Book a seat")
    print("3. Cancel a booking")
    print("4. Check your bookings")
    print("5. Exit")
    option = input()
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
def normal_user():
    from userManager import new_user, login
    print("Are you a new user? (Y/N)")
    response = input()
    if response.lower() == "y":
        new_user()
        display_menu()  # Call display_menu() after new_user()
    elif response.lower() == "n":
        login()
        display_menu()  # Call display_menu() after login()
    else:
        print("Invalid option. Please try again.")
        normal_user()

# Function to handle admin login
def admin_login():
    from adminUser import admin_display_menu
    print("Welcome, admin!")
    print("Please enter the admin password:")
    password = input()
    if password == "admin":
        print("Access granted!")
        admin_display_menu()
    else:
        print("Incorrect password. Access denied.")
        admin_login()

# Main function to start the program
def main():
    from seatingManager import is_file_empty
    is_file_empty()
    print("Welcome to the cinema booking system! Are you a normal user or an admin? (normal/admin)")
    user_type = input()
    if user_type == "normal":
        normal_user()
    elif user_type == "admin":
        admin_login()
    else:
        print("Invalid option. Please try again.")
        main()

# Entry point of the program
if __name__ == "__main__":
    main()