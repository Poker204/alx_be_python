# pattern_drawing.py

# Prompt user for size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print each column in the row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after a row is complete
    row += 1
