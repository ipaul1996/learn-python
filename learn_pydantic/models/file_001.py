from pydantic import BaseModel, ConfigDict


class User(BaseModel):
    id: int
    name: str = "Jane Doe"

    model_config = ConfigDict(str_max_length=10)


user = User(id="113")

print(user)  # id=113 name='Jane Doe'

print(user.name == "Jane Doe")  # True
print(user.id == 113)  # True
print(isinstance(user.id, int))  # True
print(user.model_dump())  # {'id': 113, 'name': 'Jane Doe'}
