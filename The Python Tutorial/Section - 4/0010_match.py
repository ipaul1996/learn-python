# A match statement takes an expression and compares its value to successive patterns 
# given as one or more case blocks. Only the first pattern that matches gets executed.

def http_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 404:
            return "Not Found"
        case 401 | 403 | 404:
            return "Not allowed"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Error"
        
point = (1, 2)

def process_point(point):
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
# The final case uses the underscore (_) as a wildcard pattern, 
# matching any value not handled by previous cases.

process_point((0, 0))
process_point((0, 5))
process_point((3, 0))
process_point((2, 3))
process_point((1, 2, 3))  # This will trigger the default case

# In match statements, patterns can assign (bind) parts of the matched value to variables,
# just like unpacking values from a tuple or list in an assignment.
def process_point(point):
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

process_point((0, 0))
process_point((0, 5))
process_point((3, 0))
process_point((2, 3))
process_point((1, 2, 3))  # This will trigger the default case


