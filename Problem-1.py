from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional


class Address(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    city: str = Field(min_length=3)
    pincode: str = Field(pattern=r"^\d{6}$")


class User(BaseModel):
    model_config = ConfigDict(validate_assignment=True)

    user_id: int
    name: str
    email: EmailStr
    age: int = Field(ge=18)
    address: Address
    is_premium: Optional[bool] = False


user = User(
    user_id=1,
    name="Dipanshu",
    email="dipanshu@google.com",
    age=24,
    address={
        "city": "Nagpur",
        "pincode":"440027"
    }
)

print(user)