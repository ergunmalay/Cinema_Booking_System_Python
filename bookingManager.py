import os


# Function to book a seat by a user
def book_seat():

    from seatingManager import load_seating_from_file, save_seating_to_file, save_user_seats, print_seating_arrangement, check_seating_price
    from Main import display_menu
    from userManager import name

    # While true and row is within the range, ask the user to enter the row number
    while True:
        try:
            row = int(input("Please enter the row number (1-7):"))
            if row < 1 or row > 7:
                print("Invalid row number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid row number. Please try again.")
            continue

    # Calculate the number of dashes for the row based on the row number entered by the user this is the number of seats in the row
    dashes = 20 - 2 * (row - 1)

    while True:
        try:
            seat = int(input("Please enter the seat number (1-" + str(dashes) + "):"))
            if seat < 1 or seat > dashes:
                print("Invalid seat number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid seat number. Please try again.")
            continue
    
    seating_arrangement = load_seating_from_file()

    # Check if the seat is already booked
    if seating_arrangement[row - 1][1][seat - 1] == "X":
        print("\nThis seat is already booked. Please select another seat.\n")
        return book_seat()
    
    # Show the price of the seat
    print("The price of the seat is: $", check_seating_price(row))

    # Confirm the booking
    while True:
        confirmation = input("Do you want to book this seat? (Y/N):")
        if confirmation.lower() == "y":
            break
        elif confirmation.lower() == "n":
            return book_seat()
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
            continue
    

    # Book the seat by marking it with an "X"
    seating_arrangement[row - 1][1] = seating_arrangement[row - 1][1][:seat - 1] + "X" + seating_arrangement[row - 1][1][seat:]

    save_seating_to_file(seating_arrangement)
    save_user_seats(name, row, seat)
    print("\nSeat booked successfully!\n\n")
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

    row = int(input("Please enter the row number (1-7) of the seat you want to cancel:")) # Get the row number of the seat to cancel
    seat = int(input("Please enter the seat number (1-"+ str(dashes) +") of the seat you want to cancel:")) # Get the seat number of the seat to cancel

    seating_arrangement = load_seating_from_file() # Load the seating arrangement from the file


    # Check if row and seat are within the range
    if not (1 <= row <= 7) or not (1 <= seat <= dashes): # If the row or seat is not within the range of the seating arrangement
        print("Invalid row or seat number. Please try again.") # Print an error message
        return cancel_booking() # Call the cancel_booking function again

    # Check if the seat is already booked
    if seating_arrangement[row - 1][1][seat - 1] == "X": # If the seat is already booked
        seating_arrangement[row - 1][1] = seating_arrangement[row - 1][1][:seat - 1] + "-" + seating_arrangement[row - 1][1][seat:] # Mark the seat as available by replacing "X" with "-"
        save_seating_to_file(seating_arrangement) # Save the updated seating arrangement to the file
        with open("user_seats.txt", "r") as file: # Open the user_seats file in read mode
            lines = file.readlines() # Read all the lines from the file
        with open("user_seats.txt", "w") as file: # Open the user_seats file in write mode
            for line in lines: # Iterate through each line in the file
                user_name, user_row, user_seat = line.strip().split(",") # Split the line into user_name, user_row, and user_seat
                if user_name == name and int(user_row) == row and int(user_seat) == seat: # If the booking matches the user's input
                    continue # Skip writing the line to the file
                file.write(line) # Write the line to the file

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

    user_seats = load_user_seats(name) # Load the bookings made by the user
    if user_seats: # If the user has bookings
        print("Here are your bookings:") # Display the user's bookings
        for row, seat in user_seats:
            print("-------------------------")
            print("Row:", row, "\nSeat:", seat, "\nPrice:", check_seating_price(row))
            print("-------------------------")
        input("Press Enter to return to the main menu...")
    else:
        print("You have no bookings.") # Print a message if the user has no bookings
        input("Press Enter to return to the main menu...")
    return display_menu()