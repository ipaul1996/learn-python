# 'while'
# The 'while' statement repeatedly executes a block of code as long as a given condition is true.
# The while loop is useful when you don't know in advance how many times you need to repeat the block.

# Basic syntax:
# while condition:
#     # code block to repeat

# Example: Counting from 0 to 4
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment count


# Example: The following while loop will continue to iterate indefinitely
# until it receives a valid number.
number = 0

while not (1 <= number <= 10):
    try:
        user_input = input("Please enter a number between 1 and 10: ")
        number = int(user_input)

        if not (1 <= number <= 10):
            print("Invalid number. Please try again.")

    except ValueError:
        print("That's not a number! Please try again.")

print(f"Great! You entered the number {number}.")
