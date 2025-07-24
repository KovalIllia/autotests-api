from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

user = UserSchema(
    id="user-id",
    email="user@gmail.com",
    lastName="Bond",
    firstName="Zara",
    middleName="Alise"
)
print(f"user: {user}")


class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

created_user = CreateUserRequestSchema(
    email="user@gmail.com",
    password="qwerty",
    lastName="Bond",
    firstName="Zara",
    middleName="Alise"
)
print(f"created user: {created_user}")


class CreatedUserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    user: UserSchema


user_data = UserSchema(
   id="user-123",
   email="user@example.com",
   lastName="Doe",
   firstName="John",
   middleName="James"
)

request_data = CreateUserRequestSchema(
   email="user@example.com",
   password="securepassword123",
   lastName="Doe",
   firstName="John",
   middleName="James"
)

response_data = CreateUserResponseSchema(
   user=UserSchema(
       id="user-123",
       email="user@example.com",
       lastName="Doe",
       firstName="John",
       middleName="James"
   )
)

print(f"User: {user_data}")
print(f"Request: {request_data}")
print(f"Response: {response_data}")
