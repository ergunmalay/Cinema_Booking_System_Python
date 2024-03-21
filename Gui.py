def create_seating(rows):
    seating = ""  # Initialize an empty string to store the seating arrangement
    for i in range(rows):
        # Add spaces before the dashes to create a pyramid-like shape
        seating += " " * (rows + i + 1)
        # Add dashes to represent the seats, with the number of dashes increasing with each row
        seating += "-" * (20 - 2 * i)
        seating += "\n"  # Add a new line after each row
    return seating

seating_selection = create_seating(8)  # Call the create_seating function with 8 rows
print(seating_selection)  # Print the resulting seating arrangement