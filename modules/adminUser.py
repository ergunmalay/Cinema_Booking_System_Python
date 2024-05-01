import os
from modules import seatingManager

# Explain the purpose of this file
# This file contains the functions that are used by the admin user to book/cancel/reset the seating arrangement
# The functions in this file are called from the admin_login function in Main.py
# The admin user can perform the following actions:
# 1. Book a seat for a user
# 2. Cancel a booking made by a user
# 3. Reset the seating arrangement
# 4. Exit the program
# Show the options like in normal users


def admin_display_menu():  # Function to display the admin menu
    # Importing functions from seatingManager.py
    # Display the current seating arrangement
    print("Here is the current seating arrangement:")
    # Load the seating arrangement from the file and display it
    seatingManager.print_seating_arrangement(
        seatingManager.load_seating_from_file())
    # Get the action input from the admin user
    action = input(
        "Would you like to book/cancel/reset or exit?\n 1.book\n2.cancel\n3.reset\n4.exit\n")
    if action == "1":  # If the action is to book a seat
        return admin_book_seat()  # Call the admin_book_seat function
    elif action == "2":  # If the action is to cancel a booking
        return admin_cancel_booking()  # Call the admin_cancel_booking function
    elif action == "3":  # If the action is to reset the seating arrangement
        return admin_reset_seating()  # Call the admin_reset_seating function
    elif action == "4":
        # If the action is to exit the program
        print("Thank you for using the cinema booking system. Goodbye!")
        exit()  # Exit the program
    else:
        print("Invalid option. Please try again.")  # If the action is invalid
        return admin_display_menu()  # Call the admin_display_menu function again


def admin_reset_seating():  # Function to reset the seating arrangement
    # Importing the create_seating_file function from seatingManager.py

    # First delete everything in the user_seats file to reset the seating arrangement
    with open("user_seats.txt", "w") as file:  # Open the user_seats file in write mode
        file.write("")  # Write an empty string to the user_seats file

    with open("seating.txt", "w") as file:  # Open the seating file in write mode
        file.write("")  # Write an empty string to the seating file

    # Call the create_seating_file function to create a new seating arrangement
    seatingManager.create_seating_file()
    # Print a message to confirm that the seating arrangement has been reset
    print("Seating arrangement reset successfully!")
    # Call the admin_display_menu function to display the admin menu again
    return admin_display_menu()


# Function to book a seat by an admin
def admin_book_seat():  # Function to book a seat by an admin
    # Importing functions from seatingManager.py
    # Get the username of the user to book the seat for
    user_name = input(
        "\nPlease enter the username of the user you want to book the seat for:")
    # Get the row number of the seat to book
    row = int(
        input("\nPlease enter the row number (1-10) of the seat you want to book:"))
    # Get the seat number of the seat to book
    seat = int(
        input("\nPlease enter the seat number (1-10) of the seat you want to book:"))

    seating_arrangement = seatingManager.load_seating_from_file()

    # Check if row and seat are within the range
    # If the row or seat is not within the range
    if not (1 <= row <= 10) or not (1 <= seat <= 10):
        # Print an error message
        print("Invalid row or seat number. Please try again.")
        return admin_book_seat()  # Call the admin_book_seat function again

    # Check if the seat is already booked
    if seating_arrangement[row - 1][1][seat - 1] == "X":
        print("This seat is already booked. Please select another seat.")
        return admin_book_seat()

    # Book the seat by marking it with an "X"
    seating_arrangement[row - 1][1] = seating_arrangement[row - 1][1][:seat - 1] + "X" + seating_arrangement[row - 1][1][seat:]

    # Save the updated seating arrangement to the file
    seatingManager.save_seating_to_file(seating_arrangement)
    # Save the booking information to the user_seats file
    seatingManager.save_user_seats(user_name, row, seat)
    print("Seat booked successfully!")  # Print a success message
    # Call the admin_display_menu function to display the admin menu again
    return admin_display_menu()

# Function to cancel a booking made by an admin


def admin_cancel_booking():
    # Importing functions from seatingManager.py

    # Get the username of the user to cancel the booking for
    user_name = input(
        "Please enter the username of the user you want to cancel the booking for:")
    # Load the bookings made by the user
    user_seats = seatingManager.load_user_seats(user_name)

    # Check if the user has any bookings and display them if they exist
    if user_seats:
        print("Here are the bookings for user:", user_name)
        for row, seat in user_seats:
            print("Row:", row, "Seat:", seat)
    else:
        print("This user has no bookings.")
        return admin_display_menu()

    # Get the row number of the seat to cancel
    row = int(
        input("Please enter the row number (1-10) of the seat you want to cancel:"))
    # Get the seat number of the seat to cancel
    seat = int(
        input("Please enter the seat number (1-10) of the seat you want to cancel:"))
    # Load the seating arrangement from the file
    seating_arrangement = seatingManager.load_seating_from_file()

    # Check if row and seat are within the range
    if not (1 <= row <= 10) or not (1 <= seat <= 10):
        print("Invalid row or seat number. Please try again.")
        return admin_cancel_booking()

    # Check if the seat is already booked by the mentioned user and cancel the booking if it is booked by another user or not booked at all by the mentioned user
    if (row, seat) in user_seats:
        # Cancel the booking by marking it with a "-"
        seating_arrangement[row - 1][1] = seating_arrangement[row -1][1][:seat - 1] + "-" + seating_arrangement[row - 1][1][seat:]
        seatingManager.save_seating_to_file(seating_arrangement)
        # Remove the booking from the user_seats file
        with open("user_seats.txt", "r") as file:
            lines = file.readlines()
        with open("user_seats.txt", "w") as file:
            for line in lines:
                user_name, user_row, user_seat = line.strip().split(",")
                if user_name == user_name and int(user_row) == row and int(user_seat) == seat:
                    continue
                file.write(line)

        print("Booking canceled successfully!")
        return admin_display_menu()
    else:
        print("This seat is not booked. Please select another seat.")
        return admin_cancel_booking()
