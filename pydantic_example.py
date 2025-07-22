from pydantic import BaseModel, Field
from typing_inspection.typing_objects import alias


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = False


# user = User(id=1, name="Alice", email="kk@gmail.com")
# print(user)


# example_2

class Address(BaseModel):
    city: str
    zip_code: str


class User_2(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    is_active: bool = False


user_2 = User_2(
    id=1,
    name="Alice",
    email="kk@gmail.com",
    address={"city": "London", "zip_code": "12345"}
)
# print(user_2)
# print(user_2.model_dump_json())


# example_3 Alias
class User_3(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias="isActive")


user_data ={
    "id":1,
    "name":"Alice",
    "email":"kk@gmail.com",
    "isActive":True
}
user_3= User_3(**user_data)
print(user_3.model_dump_json())