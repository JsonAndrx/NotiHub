from pydantic import BaseModel, EmailStr, Field


class RegisterInput(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    phone: str 


class RegisterOutput(BaseModel):
    username: str
    email: EmailStr