# Annotated
# In Python’s typing module, Annotated lets you wrap a type with extra metadata without changing the type’s behavior.
from typing import Annotated

# Basic form: Annotated[Type, metadata1, metadata2, …]
MyType = Annotated[int, "positive", {"max": 100}, "My Own Type"]

# Base type: The first argument (int above) is the actual data type.
# Annotations/metadata: All further arguments are arbitrary values that tools 
# (e.g., validators, serializers, documentation generators) can inspect at runtime or during static analysis.

from typing import Annotated
from pydantic import BaseModel, Field

class User(BaseModel):
    # Here, Annotated[int, Field(gt=0, description="User ID must be positive")]
    # tells Pydantic to enforce >0 and include a description for docs.
    user_id: Annotated[int, Field(gt=0, description="User ID must be positive")]
    name: str

# Usage:
u = User(user_id=5, name="Alice")    # OK
u = User(user_id=-1, name="Bob")     # ValidationError: value is not > 0
