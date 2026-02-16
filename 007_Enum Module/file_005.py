# Mixing Built-in Types with Enum
# ================================

# When you mix a built-in type (str, int, float, etc.) with Enum, the enum members
# become instances of BOTH the built-in type AND the Enum class. This is achieved
# using multiple inheritance.

# Syntax: class MyEnum(BuiltInType, Enum)
#         The built-in type MUST come first in the inheritance order.

# Benefits:
# - Members can be used directly where the underlying type is expected
# - Automatic type conversion in function calls, JSON serialization, etc.
# - Retains Enum benefits: iteration, membership testing, type safety
# - No need to manually access .value for type compatibility

# Common use cases:
# - String enums: API endpoints, database field values, configuration options
# - Integer enums: HTTP status codes, error codes, priority levels
# - Float enums: Mathematical constants, threshold values


from enum import Enum


class ModelName(str, Enum):
    """
    An enum that mixes in str, making members instances of both str and Enum.
    This is useful when you need predefined options that should behave like strings.
    """
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"


# Key behaviors of mixed-type enums:

# Behavior 1: Enum representation
print(ModelName.ALEXNET)  # Output: ModelName.alexnet

# Behavior 2: Accessing the underlying value
print(ModelName.ALEXNET.value)  # 'alexnet' (the actual string)

# Behavior 3: Multiple inheritance verification
print(isinstance(ModelName.ALEXNET, str))  # Output: True (is a string)
print(isinstance(ModelName.ALEXNET, Enum))  # Output: True (is also an enum)
print(type(ModelName.ALEXNET))  # <enum 'ModelName'> (primary type)
print(type(ModelName.ALEXNET).__mro__)


# Behavior 4: Direct use where string is expected (no .value needed)
def load_model(name: str):
    """Function expects a string parameter."""
    print(f"Loading {name}...")


load_model(ModelName.RESNET)  # Output: "Loading resnet..."
# The enum member is automatically treated as its string value

# This is equivalent to:
load_model(ModelName.RESNET.value)  # Also works, but .value is redundant

# Behavior 5: String operations work directly
print(ModelName.LENET.upper())  # "LENET" (inherits str methods)
print(ModelName.ALEXNET.startswith("alex"))  # True
print(f"Model: {ModelName.RESNET}")  # "Model: resnet" (auto-converts in f-strings)

# Behavior 6: Equality comparisons
print(ModelName.LENET == ModelName("lenet"))  # True (enum lookup by value)
print(ModelName.LENET == "lenet")  # True (compares with string directly!)
print(ModelName.LENET is ModelName.LENET)  # True (singleton - same object)

# Important: String comparison works because of str mixin
# With plain Enum, ModelName.LENET == "lenet" would be False


# Behavior 7: Serialization advantage
import json

# Plain Enum requires .value:
# json.dumps({"model": Color.RED})  # Would fail (Color.RED not JSON serializable)

# String Enum works automatically:
data = {"model": ModelName.ALEXNET}
json_str = json.dumps(data)
print(json_str)  # {"model": "alexnet"} (automatically serialized!)


class HttpStatus(int, Enum):
    """
    An enum that mixes in int, making members behave like integers.
    Useful for status codes, flags, or other numeric constants.
    """

    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    SERVER_ERROR = 500


# Integer enum members inherit all int behaviors:
print(HttpStatus.OK)  # HttpStatus.OK (enum representation)
print(HttpStatus.OK.value)  # 200 (underlying integer)
print(isinstance(HttpStatus.OK, int))  # True (is an integer)
print(isinstance(HttpStatus.OK, Enum))  # True (is also an enum)


# Mathematical operations work directly (because it's an int!)
print(HttpStatus.SERVER_ERROR + 1)  # 501
print(HttpStatus.OK * 2)  # 400
print(HttpStatus.NOT_FOUND // 2)  # 202

# Comparison with integers works directly
response_code = 404
if response_code == HttpStatus.NOT_FOUND:
    print("Page not found!")  # This prints!

# Multiple ways to check status:
print(HttpStatus.OK == 200)  # True (int comparison)
print(HttpStatus.OK is HttpStatus(200))  # True (enum lookup by value)
print(200 in HttpStatus)  # False! (200 is not a member, HttpStatus.OK is)


# Use in range checks
def is_success(status: int) -> bool:
    """Check if HTTP status indicates success."""
    return 200 <= status < 300


print(is_success(HttpStatus.OK))  # True (enum used as int)
print(is_success(HttpStatus.CREATED))  # True


# JSON serialization advantage
response = {"status": HttpStatus.OK, "code": HttpStatus.NOT_FOUND}
print(json.dumps(response))
# {"status": 200, "code": 404} (automatically serialized as integers!)


# Sorting and ordering work
statuses = [HttpStatus.SERVER_ERROR, HttpStatus.OK, HttpStatus.NOT_FOUND]
sorted_statuses = sorted(statuses)
print(sorted_statuses)
# [HttpStatus.OK, HttpStatus.NOT_FOUND, HttpStatus.SERVER_ERROR]
# Sorted by integer value: 200, 404, 500
