# __init__
# Called after the instance is created and used to initialize instance attributes.
# Signature: def __init__(self, *args, **kwargs) -> None

# Use Cases:
# - Set up instance attributes (self.x = …).
# - Validate or transform arguments.
# - Raise errors if something’s invalid.


class Point:
    def __init__(self, x, y):
        # store coordinates
        self.x = float(x)
        self.y = float(y)


p = Point(2, 3)
print(p.x, p.y)  # → 2.0 3.0
