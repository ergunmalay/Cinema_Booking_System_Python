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

def book_seat():
    print("Please enter the row number (1-10):")
    row = int(input())
    print("Please enter the seat number (1-10):")
    seat = int(input())

    seating_arrangement = load_seating_from_file()

    # Check if row and seat are within the range
    if not (1 <= row <= 10) or not (1 <= seat <= 10):
        print("Invalid row or seat number. Please try again.")
        return book_seat()

    # Check if the seat is already booked
    if seating_arrangement[row - 1][1][seat - 1] == "X":
        print("This seat is already booked. Please select another seat.")
        return book_seat()

    # Book the seat by marking it with an "X"
    seating_arrangement[row - 1][1] = seating_arrangement[row - 1][1][:seat - 1] + "X" + seating_arrangement[row - 1][1][seat:]

    save_seating_to_file(seating_arrangement)
    save_user_seats(name, row, seat)
    print("Seat booked successfully!")
    return display_menu()

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

def load_user_seats(name):
    user_seats = []
    with open("user_seats.txt", "r") as file:
        for line in file:
            user_name, row, seat = line.strip().split(",")
            if user_name == name:
                user_seats.append((int(row), int(seat)))
    return user_seats

def cancel_booking():
    print("Here are your bookings:") # Display the user's bookings
    user_seats = load_user_seats(name)
    if user_seats:
        for row, seat in user_seats:
            print("Row:", row, "Seat:", seat)
    else:
        print("You have no bookings.")
        return display_menu()
    
    # Show the seating arrangement
    print("Here is the current seating arrangement:")
    
    # Load the seating arrangement from the file and replace the booked seats with "B"
    seating_arrangement = load_seating_from_file()
    for row, seat in user_seats:
        seating_arrangement[row - 1][1] = seating_arrangement[row - 1][1][:seat - 1] + "B" + seating_arrangement[row - 1][1][seat:]
    print_seating_arrangement(seating_arrangement)

    print("Please enter the row number (1-10) of the seat you want to cancel:")
    row = int(input())
    print("Please enter the seat number (1-10) of the seat you want to cancel:")
    seat = int(input())

    seating_arrangement = load_seating_from_file()

    # Check if row and seat are within the range
    if not (1 <= row <= 10) or not (1 <= seat <= 10):
        print("Invalid row or seat number. Please try again.")
        return cancel_booking()

    # Check if the seat is already booked
    if seating_arrangement[row - 1][1][seat - 1] == "X":
        # Cancel the booking by marking it with a "-"
        seating_arrangement[row - 1][1] = seating_arrangement[row - 1][1][:seat - 1] + "-" + seating_arrangement[row - 1][1][seat:]
        save_seating_to_file(seating_arrangement)
        # Remove the booking from the user_seats file
        with open("user_seats.txt", "r") as file:
            lines = file.readlines()
        with open("user_seats.txt", "w") as file:
            for line in lines:
                user_name, user_row, user_seat = line.strip().split(",")
                if user_name == name and int(user_row) == row and int(user_seat) == seat:
                    continue
                file.write(line)

        print("Booking canceled successfully!")
        return display_seating()
    else:
        print("This seat is not booked. Please select another seat.")
        return cancel_booking()

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

def create_seating_file():
    with open("seating.txt", "w") as file:
        dashes = 20
        for i in range(7):
            # Add spaces at the start of the line
            line = " " * i + "-" * dashes + "\n"
            file.write(line)
            dashes -= 2

def display_seating():
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
    
def check_seating_price(row):
    case = { 1:'£100', 2:'£80', 3:'£70', 4:'£70', 5:'£60', 6:'£40', 7:'£20' }
    return case.get(row)

def check_bookings():
    user_seats = load_user_seats(name)
    if user_seats:
        print("Here are your bookings:")
        for row, seat in user_seats:
            print("-------------------------")
            print("Row:", row, "\nSeat:", seat, "\nPrice:",check_seating_price(row))
            print("-------------------------")
    else:
        print("You have no bookings.")
    return display_menu()

def display_menu():
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


def print_seating_arrangement(seating_arrangement):
    for row in seating_arrangement:
        print(row[0] + row[1])

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

def save_seating_to_file(seating_arrangement):
    with open("seating.txt", "w") as file:
        for row in seating_arrangement:
            # Add leading spaces to row before saving to file
            leading_spaces = row[0]
            file.write(" " * len(leading_spaces) + row[1] + "\n")

def main():
    is_file_empty()
    print("Are you a new user? (Y/N)")
    response = input()
    if response.lower() == "y":
        new_user()
        display_menu()  # Call display_menu() after new_user()
    else:
        login()
        display_menu()  # Call display_menu() after login()

if __name__ == "__main__":
    main()
