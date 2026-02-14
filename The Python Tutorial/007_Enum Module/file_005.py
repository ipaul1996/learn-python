# Mixing in built-in types (e.g., str, int) with Enum creates enum members that
# inherit behavior from both the built-in type and the Enum class. This allows
# enum members to be used interchangeably with their underlying values while
# maintaining the benefits of enumeration (type safety, limited options, etc.).

from enum import Enum

class ModelName(str, Enum):
    """
    An enum that mixes in str, making members instances of both str and Enum.
    This is useful when you need predefined options that should behave like strings.
    """
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# Key behaviors of mixed-type enums:

# 1. Accessing members returns the enum representation:
print(ModelName.alexnet)        # Output: ModelName.alexnet

# 2. The .value attribute provides access to the underlying value:
print(ModelName.alexnet.value)  # Output: 'alexnet'

# 3. Members inherit from the mixed-in type (str in this case):
print(isinstance(ModelName.alexnet, str))  # Output: True
print(isinstance(ModelName.alexnet, Enum)) # Output: True

# 4. Members can be used directly where the underlying type is expected:
def load_model(name: str):
    print(f"Loading {name}...")

load_model(ModelName.resnet)  # Output: "Loading resnet..."
# Note: The enum is automatically converted to its string value

# 5. Equality comparisons work with both enum members and underlying values:
print(ModelName.lenet == ModelName("lenet"))  # True (enum comparison)
print(ModelName.lenet == "lenet")             # True (string comparison)
print(ModelName.lenet is ModelName.lenet)     # True (identity comparison)


class HttpStatus(int, Enum):
    """
    An enum that mixes in int, making members behave like integers.
    Useful for status codes, flags, or other numeric constants.
    """
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500


# Integer enum members inherit all int behaviors:
print(HttpStatus.OK)           # Output: HttpStatus.OK
print(HttpStatus.OK.value)     # Output: 200
print(isinstance(HttpStatus.OK, int))  # Output: True

# Can be used in mathematical operations:
print(HttpStatus.SERVER_ERROR + 1)  # Output: 501

# Can be compared directly with integers:
print(HttpStatus.NOT_FOUND == 404)  # Output: True

# Useful for serialization (e.g., JSON conversion):
import json
print(json.dumps({"status": HttpStatus.OK}))  # Output: {"status": 200}

