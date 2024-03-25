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

def print_seating_arrangement(seating_arrangement):
    for row in seating_arrangement:
        print(row[0] + row[1])

print_seating_arrangement(seating_arrangement)