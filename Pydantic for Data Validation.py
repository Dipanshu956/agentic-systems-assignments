from pydantic import BaseModel, EmailStr, Field

class UserRegister(BaseModel):
    username: str = Field(min_length=5)
    email: EmailStr
    age: int = Field(ge=18)


# Example Valid Input
user = UserRegister(
    username="Dipanshu",
    email="dipanshu@gmail.com",
    age=24
)

print(user)