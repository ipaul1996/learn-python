# A `match` statement takes a "subject" (data) and compares its structure against a series
# of "patterns" (shapes). It executes the code block of the FIRST matching case.

# - Subject: The data you are analyzing (following the `match` keyword).
# - Pattern: The rule or shape in a `case` clause (e.g., a specific value, a list of size 2, etc.).
# - Binding: The process of assigning parts of the matched data to variable names for use.

# Pattern Types Overview:
# 1. Literal Pattern: Checks for exact equality (e.g., case 404:).
# 2. Capture Pattern: Matches anything and assigns it to a variable name (e.g., case x:).
# 3. Wildcard Pattern (_): A "catch-all" that matches anything but throws the value away.
#    Used for the default/fallback case.
# 4. OR Pattern (|): Matches if the subject fits any of the options (e.g., case 401 | 403:).
# 5. Sequence Pattern: Matches lists or tuples by length and content. Can extract items.
#    (e.g., case [x, y]: matches a list of exactly 2 items).
# 6. Class Pattern: Checks if the subject is an instance of a Class and extracts attributes.
#    (e.g., case Point(x=x, y=y):).
# 7. Guard: An extra `if` condition attached to a case. The pattern must match AND
#    the condition must be True for the case to run.


# Basic Literals and OR Patterns
def http_error(status):
    match status:
        # Literal Pattern: Matches exact value 400
        case 400:
            return "Bad Request"
        # Literal Pattern: Matches exact value 404
        case 404:
            return "Not Found"
        # OR Pattern: Matches if status is 401 OR 403 OR 418
        case 401 | 403 | 418:
            return "Not allowed"
        # Wildcard Pattern: Matches anything not caught above (Default)
        case _:
            return "Unknown Error"


# Sequence Patterns (Structure Matching)
def process_point(point):
    match point:
        # Matches a tuple with exactly two items, both being 0.
        case (0, 0):
            print("Origin")
        # Matches a tuple of 2 items where the first is 0.
        # Binds the second item to variable 'y'.
        case (0, y):
            print(f"Y-axis at {y}")
        # Matches a tuple of 2 items where the second is 0.
        # Binds the first item to variable 'x'.
        case (x, 0):
            print(f"X-axis at {x}")
        # Matches ANY tuple of exactly 2 items.
        # Binds them to 'x' and 'y'.
        case (x, y):
            print(f"Point at ({x}, {y})")
        # Default: Matches anything that isn't a 2-item tuple.
        case _:
            print("Unknown point format")


process_point((0, 0))  # Matches first case
process_point((0, 5))  # Matches second case
process_point((3, 0))  # Matches third case
process_point((2, 3))  # Matches fourth case
process_point((1, 2, 3))  # Triggers default (tuple has 3 items, not 2)


# Guards (Conditional Matching)
def process_guarded_point(point):
    match point:
        # 1. Checks if it is a 2-item sequence (x, y).
        # 2. THEN checks if x equals y.
        case (x, y) if x == y:
            print(f"Point ({x}, {y}) is on the y=x diagonal.")
        # Matches 2-item sequence if the Guard above failed.
        case (x, y):
            print(f"Point ({x}, {y}) is not on the diagonal.")
        case _:
            print("Subject is not a 2-element sequence.")


process_guarded_point((3, 3))  # Matches first case
process_guarded_point((3, 4))  # Matches second case


# Class Patterns (Object Matching)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_point(obj):
    match obj:
        # Checks if obj is instance of Point AND if x==0 and y==0
        case Point(x=0, y=0):
            print("Point is at the origin")
        # Checks if obj is instance of Point.
        # Captures the attribute 'x' into variable 'x_val'.
        # Captures the attribute 'y' into variable 'y_val'.
        case Point(x=x_val, y=y_val):
            print(f"Point is at ({x_val}, {y_val})")
        case _:
            print("Not a Point")


p = Point(1, 2)
check_point(p)  # Output: Point is at (1, 2)


# Strict Type Matching (List vs Tuple)
def process_sequence(seq):
    match seq:
        # This pattern requires THREE things:
        # 1. It must be a LIST (brackets [] matter). A tuple won't match.
        # 2. It must have exactly 3 elements.
        # 3. The second element must be exactly 0.
        # If valid, it binds the first element to 'x'.
        case [x, 0, _]:
            print(f"Match! First element is {x}, and the second is 0.")
        case _:
            print("No match.")


process_sequence(["hello", 0, 100])  # Match! (List, 3 items, middle is 0)
process_sequence([99, 0, "world"])  # Match!
process_sequence([1, 2, 3])  # No match. (Middle is 2, not 0)
process_sequence(["a", 0])  # No match. (Length is 2, not 3)
process_sequence(("a", 0, "b"))  # No match. (It is a Tuple, pattern expects List)
