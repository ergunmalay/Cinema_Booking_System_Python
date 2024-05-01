import os
from modules import userManager, bookingManager
import Main

# Function to save the booked seats of a user to a file

# Add file opening Exception to each file opening


def save_user_seats(name, row, seat):
    # Check if the file exists
    if not os.path.exists("user_seats.txt"):
        with open("user_seats.txt", "w"):  # Create the file if it does not exist
            pass  # Do nothing if the file already exists

    # Write the user's name, row, and seat to the file
    with open("user_seats.txt", "a") as file:
        # Check if the user is already in the file and add the new seat to the existing user entry if they are found
        # Load the user's seats from the file
        user_seats = load_user_seats(name)
        for user_row, user_seat in user_seats:  # Iterate through the user's seats
            if user_row == row and user_seat == seat:  # Check if the seat is already booked
                return  # Return if the seat is already booked
        # Write the user's name, row, and seat to the file
        file.write(name + "," + str(row) + "," + str(seat) + "\n")

# Function to load the booked seats of a user from a file


def load_user_seats(name):
    user_seats = []  # Initialize an empty list to store the user's seats
    with open("user_seats.txt", "r") as file:  # Open the file in read mode
        for line in file:  # Iterate through each line in the file
            # Split the line into user name, row, and seat
            user_name, row, seat = line.strip().split(",")
            if user_name == name:  # Check if the user name matches the input name
                # Append the row and seat to the user_seats list
                user_seats.append((int(row), int(seat)))
    return user_seats

# Function to put user_seats back into the seating arrangement file


def put_user_seats_back():  # Function to put user_seats back into the seating arrangement file
    # Load the seating arrangement from the file
    seating_arrangement = load_seating_from_file()
    with open("user_seats.txt", "r") as file:  # Open the user_seats file in read mode
        for line in file:  # Iterate through each line in the file
            # Split the line into user name, row, and seat
            user_name, row, seat = line.strip().split(",")
            seating_arrangement[int(row) - 1][1] = seating_arrangement[int(row) - 1][1][:int(
                seat) - 1] + "X" + seating_arrangement[int(row) - 1][1][int(seat):]
    # Save the updated seating arrangement to the file
    save_seating_to_file(seating_arrangement)

# Function to check if the seating arrangement file is empty


def is_file_empty():  # Function to check if the seating arrangement file is empty

    userManager.check_seating_file()  # Check if the seating arrangement file exists

    # Check if the seating arrangement is empty
    with open("seating.txt", "r") as file:  # Open the file in read mode
        for line in file:  # Iterate through each line in the file
            if line.strip():  # Check if the line is not empty
                return  # Return if the seating arrangement is not empty

    # If the seating arrangement is empty, recreate it
    create_seating_file()  # Create the seating arrangement file

# Function to create the seating arrangement file with initial seats


def create_seating_file():  # Function to create the seating arrangement file with initial seats
    with open("seating.txt", "w") as file:  # Open the file in write mode
        dashes = 20  # Initialize the number of dashes for the first row
        for i in range(7):  # Iterate through the rows
            # Add spaces at the start of the line
            # Create the line with leading spaces and dashes
            line = " " * i + "-" * dashes + "\n"
            file.write(line)  # Write the line to the file
            dashes -= 2  # Decrement the number of dashes for the next row

    # Call put_user_seats_back() after create_seating_file() to put the user seats back into the seating arrangement
    put_user_seats_back()


# Function to display the seating arrangement to the user
def display_seating():  # Function to display the seating arrangement to the user
    # Print the message to the user
    print("Here is the current seating arrangement:")
    # Print the seating arrangement to the console
    print_seating_arrangement(load_seating_from_file())
    # Ask the user for the next action
    action = input("Would you like to book a seat, cancel a booking, or exit the program? \n1. book\n2. cancel\n3. Back🔙\n\n")  # Get the user's input
    if action == "1":  # If the user wants to book a seat
        return bookingManager.book_seat()  # Call the book_seat() function
    elif action == "2":  # If the user wants to cancel a booking
        return bookingManager.cancel_booking()  # Call the cancel_booking() function
    elif action == "3":  # If the user wants to exit the program
        # Print the exit message
        print("Thank you for using the cinema booking system. Goodbye!")
        return Main.display_menu()  # Call the display_menu() function from Main.py
    else:
        print("Invalid option. Please try again.")
        return display_seating()

# Function to check the price of a seat based on its row
def check_seating_price(row):
    case = {1: '£100', 2: '£80', 3: '£70',
            4: '£70', 5: '£60', 6: '£40', 7: '£20'}  # Define the price for each row
    return case.get(row)  # Return the price based on the row

# Function to print the seating arrangement to the console


def print_seating_arrangement(seating_arrangement):
    for row in seating_arrangement:
        print(row[0] + row[1])

# Function to load the seating arrangement from the file


def load_seating_from_file():
    seating_arrangement = []
    with open("seating.txt", "r") as file:
        line_number = 1
        for line in file:
            # Remove newline character and split the line into characters
            row = list(line.strip())
            # Determine the number of leading spaces based on the line number
            leading_spaces = line_number - 1
            # Append row to seating arrangement while preserving leading spaces
            seating_arrangement.append([' ' * leading_spaces, ''.join(row)])
            line_number += 1
    return seating_arrangement

# Function to save the seating arrangement to the file


def save_seating_to_file(seating_arrangement):
    with open("seating.txt", "w") as file:
        for row in seating_arrangement:
            # Add leading spaces to row before saving to file
            leading_spaces = row[0]
            file.write(" " * len(leading_spaces) + row[1] + "\n")
