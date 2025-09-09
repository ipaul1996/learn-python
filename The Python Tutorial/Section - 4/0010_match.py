# A match statement evaluates a subject expression and compares its value against a series
# of patterns in sequential case clauses. Execution is committed to the code block of the
# first `case` clause whose pattern successfully matches the subject.
# - Subject: The expression following match whose value is to be matched.
# - Pattern: The structure following a case clause, used to test the subject.
# - Binding: The assignment of parts of the subject's value to variables within a pattern.

# Pattern Types
# 1. Literal Pattern: Matches an exact literal value (e.g., 404, "Not Found", None).
# 2. Capture Pattern: Matches any value and binds it to a variable (e.g., case x:).
# 3. Wildcard Pattern (_): A special pattern that always matches but never binds a value.
#    It's used as a "catch-all" or default case.
# 4. OR Pattern (|): Combines several patterns into a single case. The case matches if the
#    subject matches any of the sub-patterns (e.g., case 401 | 403:).
# 5. Sequence Pattern: Matches sequences like lists or tuples and can deconstruct them.
#    It works well with capture, literal, and wildcard patterns (e.g., case [x, 0, _]:).
# 6. Class Pattern: Matches instances of a specific class and can capture attribute values.
#    This is key for working with objects (e.g., case Point(x=x_val, y=y_val):).
# 7. Guard: An optional if condition added to a pattern. The case only matches if the pattern
#    matches and the guard expression is true (e.g., case (x, y) if x > y:).


def http_error(status):
    match status:
        # Literal Pattern
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        # OR Pattern
        case 401 | 403 | 404:
            return "Not allowed"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Error"


def process_point(point):
    match point:
        # Sequence pattern with two literal patterns.
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y-axis at {y}")
        case (x, 0):
            print(f"X-axis at {x}")
        case (x, y):
            print(f"Point at ({x}, {y})")
        case _:
            print("Unknown point format")


# The final case uses the underscore (_) as a wildcard pattern,
# matching any value not handled by previous cases.

process_point((0, 0))
process_point((0, 5))
process_point((3, 0))
process_point((2, 3))
process_point((1, 2, 3))  # This will trigger the default case


# In match statements, patterns can assign (bind) parts of the matched value to variables,
# just like unpacking values from a tuple or list in an assignment.
def process_point1(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y-axis at {y}")
        case (x, 0):
            print(f"X-axis at {x}")
        case (x, y):
            print(f"Point at ({x}, {y})")
        case _:
            print("Unknown point format")


# The first pattern has two literals. But the next two patterns combine a literal and
# a variable, and the variable binds a value from the subject (point). The fourth
# pattern captures two values, which makes it conceptually similar to the unpacking assignment (x, y) = point.

process_point1((0, 0))
process_point1((0, 5))
process_point1((3, 0))
process_point1((2, 3))
process_point1((1, 2, 3))  # This will trigger the default case


def process_guarded_point(point):
    match point:
        # Sequence pattern with a guard.
        case (x, y) if x == y:
            print(f"Point ({x}, {y}) is on the y=x diagonal.")
        case (x, y):
            print(f"Point ({x}, {y}) is not on the diagonal.")
        case _:
            print("Subject is not a 2-element sequence.")


process_guarded_point((3, 3))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_point(obj):
    match obj:
        case Point(x=0, y=0):  # Class pattern with literal patterns inside
            print("Point is at the origin")
        case Point(x=x_val, y=y_val):  # Class pattern that captures attributes
            print(f"Point is at ({x_val}, {y_val})")
        case _:
            print("Not a Point")


p = Point(1, 2)
check_point(p)  # Point is at (1, 2)


def process_sequence(seq):
    match seq:
        case [x, 0, _]:
            print(f"Match! First element is {x}, and the second is 0.")
        case _:
            print("No match.")


process_sequence(
    ["hello", 0, 100]
)  # Match! First element is hello, and the second is 0.
process_sequence([99, 0, "world"])  # Match! First element is 99, and the second is 0.
process_sequence([1, 2, 3])  # No match. (The second element is not 0)
process_sequence(["a", 0])  # No match. (The list does not have three elements)
process_sequence(("a", 0, "b"))  # No match. (This is a tuple, not a list)
