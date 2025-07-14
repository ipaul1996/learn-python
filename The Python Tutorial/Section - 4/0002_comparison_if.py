# Comparison Operators and if Statements
# Comparison operators are used to compare two values and return a boolean result (True or False).
# The common comparison operators in Python are:
# == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to).


x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print("Negative changed to zero")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

# There can be zero or more elif parts, and the else part is optional.
# The condition in the if statement is evaluated first. If it is true, the block of code under it is executed.
# If it is false, the next elif condition is checked, and so on.
# If none of the conditions are true, the else block is executed if it exists.


# The if statement can also be used to check for multiple conditions using logical operators like and, or, and not.
y = int(input("Please enter another integer: "))

if x > 0 and y > 0:
    print("Both numbers are positive")
elif x > 0 or y > 0:
    print("At least one number is positive")
else:
    print("Neither number is positive")



# The if statement can also be used to check for equality using the == operator, or inequality using the != operator.
a = int(input("Enter first number for equality check: "))
b = int(input("Enter second number for equality check: "))

if a == b:
    print("The numbers are equal.")
elif a != b:
    print("The numbers are not equal.")



# The if statement can be used to check for membership in a list, tuple, or set using the in operator.
numbers = [1, 2, 3, 4, 5]
num = int(input("Enter a number to check membership in the list [1, 2, 3, 4, 5]: "))
if num in numbers:
    print(f"{num} is in the list.")
else:
    print(f"{num} is not in the list.")




