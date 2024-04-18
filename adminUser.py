import os

# Function to display admin menu options
def admin_display_menu():
    from seatingManager import print_seating_arrangement, load_seating_from_file, create_seating_file
    print("Here is the current seating arrangement:")
    print_seating_arrangement(load_seating_from_file())
    print("Would you like to book/cancel/reset or exit? (book/cancel/reset/exit)")
    action = input()
    if action == "book":
        return admin_book_seat()
    elif action == "cancel":
        return admin_cancel_booking()
    elif action == "reset":
        return admin_reset_seating()
    elif action == "exit":
        print("Thank you for using the cinema booking system. Goodbye!")
        exit()
    else:
        print("Invalid option. Please try again.")
        return admin_display_menu()
    
def admin_reset_seating():
    from seatingManager import create_seating_file

    # First delete everything in the user_seats file to reset the seating arrangement
    with open("user_seats.txt", "w") as file:
        file.write("")
    
    with open("seating.txt", "w") as file:
        file.write("")
    
    create_seating_file()
    print("Seating arrangement reset successfully!")
    return admin_display_menu()




# Function to book a seat by an admin
def admin_book_seat():
    from seatingManager import load_seating_from_file, save_seating_to_file, save_user_seats

    print("Please enter the username of the user you want to book the seat for:")
    user_name = input()
    print("Please enter the row number (1-10) of the seat you want to book:")
    row = int(input())
    print("Please enter the seat number (1-10) of the seat you want to book:")
    seat = int(input())

    seating_arrangement = load_seating_from_file()

    # Check if row and seat are within the range
    if not (1 <= row <= 10) or not (1 <= seat <= 10):
        print("Invalid row or seat number. Please try again.")
        return admin_book_seat()

    # Check if the seat is already booked
    if seating_arrangement[row - 1][1][seat - 1] == "X":
        print("This seat is already booked. Please select another seat.")
        return admin_book_seat()

    # Book the seat by marking it with an "X"
    seating_arrangement[row - 1][1] = seating_arrangement[row - 1][1][:seat - 1] + "X" + seating_arrangement[row - 1][1][seat:]

    save_seating_to_file(seating_arrangement)
    save_user_seats(user_name, row, seat)
    print("Seat booked successfully!")
    return admin_display_menu()

# Function to cancel a booking made by an admin
def admin_cancel_booking():
    from seatingManager import load_user_seats, load_seating_from_file, save_seating_to_file

    print("Please enter the username of the user you want to cancel the booking for:")
    user_name = input()
    user_seats = load_user_seats(user_name)

    if user_seats:
        print("Here are the bookings for user:", user_name)
        for row, seat in user_seats:
            print("Row:", row, "Seat:", seat)
    else:
        print("This user has no bookings.")
        return admin_display_menu()

    print("Please enter the row number (1-10) of the seat you want to cancel:")
    row = int(input())
    print("Please enter the seat number (1-10) of the seat you want to cancel:")
    seat = int(input())
    seating_arrangement = load_seating_from_file()

    # Check if row and seat are within the range
    if not (1 <= row <= 10) or not (1 <= seat <= 10):
        print("Invalid row or seat number. Please try again.")
        return admin_cancel_booking()

    # Check if the seat is already booked by the mentioned user and cancel the booking if it is booked by another user or not booked at all by the mentioned user
    if (row, seat) in user_seats:
        # Cancel the booking by marking it with a "-"
        seating_arrangement[row - 1][1] = seating_arrangement[row - 1][1][:seat - 1] + "-" + seating_arrangement[row - 1][1][seat:]
        save_seating_to_file(seating_arrangement)
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