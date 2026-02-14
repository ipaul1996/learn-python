# The break statement breaks out of the innermost enclosing for or while loop.
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
"""
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
"""

# The continue statement continues with the next iteration of the loop, skipping the current one:
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

"""
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
"""

# In a for or while loop the break statement may be paired with an else clause.
# If the loop finishes without executing the break, the else clause executes, otherwise not.
# Of course, other ways of ending the loop early, such as a return or a raised exception,
# will also skip execution of the else clause.
# Here the metal model for else block should be thought of as nobreak i.e., normal loop completion
# without executing the break statement.

# Example 1: for-else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        # loop fell through without finding a factor
        print(f"{n} is a prime number")

"""
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
"""

# Example 2: while-else
n = 2
while n < 10:
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number")
    n += 1

"""
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
"""


"""
For Loops: Normal termination means the iterator is exhausted (it ran out of items).
While Loops: Normal termination means the condition became false.
For both of the above cases, else block will not be executed.
"""
