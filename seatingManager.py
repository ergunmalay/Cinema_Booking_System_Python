import os

# Function to save the booked seats of a user to a file
def save_user_seats(name, row, seat):
    # Check if the file exists
    if not os.path.exists("user_seats.txt"):
        with open("user_seats.txt", "w"):
            pass

    # Write the user's name, row, and seat to the file
    with open("user_seats.txt", "a") as file:
        # Check if the user is already in the file and add the new seat to the existing user entry if they are found
        user_seats = load_user_seats(name)
        for user_row, user_seat in user_seats:
            if user_row == row and user_seat == seat:
                return
        file.write(name + "," + str(row) + "," + str(seat) + "\n")

# Function to load the booked seats of a user from a file
def load_user_seats(name):
    user_seats = []
    with open("user_seats.txt", "r") as file:
        for line in file:
            user_name, row, seat = line.strip().split(",")
            if user_name == name:
                user_seats.append((int(row), int(seat)))
    return user_seats

# Function to put user_seats back into the seating arrangement file
def put_user_seats_back():
    seating_arrangement = load_seating_from_file()
    with open("user_seats.txt", "r") as file:
        for line in file:
            user_name, row, seat = line.strip().split(",")
            seating_arrangement[int(row) - 1][1] = seating_arrangement[int(row) - 1][1][:int(seat) - 1] + "X" + seating_arrangement[int(row) - 1][1][int(seat):]
    save_seating_to_file(seating_arrangement)

# Function to check if the seating arrangement file is empty
def is_file_empty():
    if not os.path.exists("seating.txt"):
        create_seating_file()
        return

    # Check if the seating arrangement is empty
    with open("seating.txt", "r") as file:
        for line in file:
            if line.strip():
                return

    # If the seating arrangement is empty, recreate it
    create_seating_file()

# Function to create the seating arrangement file with initial seats
def create_seating_file():
    with open("seating.txt", "w") as file:
        dashes = 20
        for i in range(7):
            # Add spaces at the start of the line
            line = " " * i + "-" * dashes + "\n"
            file.write(line)
            dashes -= 2

    put_user_seats_back() # Call put_user_seats_back() after create_seating_file() to put the user seats back into the seating arrangement



# Function to display the seating arrangement to the user
def display_seating():
    from bookingManager import book_seat, cancel_booking

    print("Here is the current seating arrangement:")
    print_seating_arrangement(load_seating_from_file())
    print("Would you like to book a seat, cancel a booking, or exit the program? (book/cancel/exit)")
    action = input()
    if action == "book":
        return book_seat()
    elif action == "cancel":
        return cancel_booking()
    elif action == "exit":
        print("Thank you for using the cinema booking system. Goodbye!")
    else:
        print("Invalid option. Please try again.")
        return display_seating()

# Function to check the price of a seat based on its row
def check_seating_price(row):
    case = {1: '£100', 2: '£80', 3: '£70',
            4: '£70', 5: '£60', 6: '£40', 7: '£20'}
    return case.get(row)

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
