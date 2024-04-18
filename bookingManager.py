import os


# Function to book a seat by a user
def book_seat():

    from seatingManager import load_seating_from_file, save_seating_to_file, save_user_seats, print_seating_arrangement, check_seating_price
    from Main import display_menu
    from userManager import name

    print("Please enter the row number (1-7):")
    row = int(input())
    # Calculate the number of dashes for the row based on the row number entered by the user this is the number of seats in the row
    dashes = 20 - 2 * (row - 1)
    print("Please enter the seat number (1-" + str(dashes) + "):")
    seat = int(input())

    seating_arrangement = load_seating_from_file()

    # Check if row and seat are within the range
    if not (1 <= row <= 7) or not (1 <= seat <= dashes):
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

# Function to cancel a booking made by a user
def cancel_booking():
    from seatingManager import load_seating_from_file, save_seating_to_file, load_user_seats, print_seating_arrangement, display_seating
    from Main import display_menu
    from userManager import name

    print("Here are your bookings:")  # Display the user's bookings
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

    dashes = 20 - 2 * (row - 1)

    print("Please enter the row number (1-7) of the seat you want to cancel:")
    row = int(input())
    print("Please enter the seat number (1-"+ str(dashes) +") of the seat you want to cancel:")
    seat = int(input())

    seating_arrangement = load_seating_from_file()


    # Check if row and seat are within the range
    if not (1 <= row <= 7) or not (1 <= seat <= dashes):
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
    
# Function to display the user's bookings
def check_bookings():
    from userManager import name
    from seatingManager import load_user_seats, check_seating_price
    from Main import display_menu

    user_seats = load_user_seats(name)
    if user_seats:
        print("Here are your bookings:")
        for row, seat in user_seats:
            print("-------------------------")
            print("Row:", row, "\nSeat:", seat, "\nPrice:", check_seating_price(row))
            print("-------------------------")
    else:
        print("You have no bookings.")
    return display_menu()