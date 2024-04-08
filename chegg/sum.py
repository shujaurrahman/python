# Open the file named Numbers.txt
try:
    with open('numbers.txt', 'r') as file:
        # Read all numbers from the file and calculate their sum
        numbers = [int(line.strip()) for line in file.readlines()]
        total_sum = sum(numbers)

        # Display the sum of all numbers
        print("Sum of all numbers:", total_sum)

except FileNotFoundError:
    print("File not found.")
