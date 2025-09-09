# Mixing in built-in types (e.g., str) to create enums whose members behave like that type:
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# Accessing members returns Enum representation:
print(ModelName.alexnet)  # ModelName.alexnet

# The `.value` attribute is the underlying string:
print(ModelName.alexnet.value)  # 'alexnet'

# Because we mixed in `str`, members are instances of `str`:
print(isinstance(ModelName.alexnet, str))  # True


# You can directly use them where strings are expected:
def load_model(name: str):
    print(f"Loading {name}...")


load_model(ModelName.resnet)  # "Loading ModelName.resnet..."

# Equality and comparisons work both as Enum and as str:
print(ModelName.lenet == ModelName("lenet"))  # True (enum identity)
print(ModelName.lenet == "lenet")  # True (str comparison)


class HttpStatus(int, Enum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500


# Members behave like integers
print(HttpStatus.OK)  # HttpStatus.OK
print(HttpStatus.OK.value)  # 200
print(isinstance(HttpStatus.OK, int))  # True

# Can compare directly to integers
print(HttpStatus.NOT_FOUND == 404)  # True

# Use in arithmetic or serialization directly
print(HttpStatus.SERVER_ERROR + 1)  # 501
