from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=30,
                          description="El username debe estar entre 3 y 30 caracteres")
    email: EmailStr
    password = str = Field(
        min_length=7, description="El password debe tener al menos 7 caracteres")
    role: Optional[str] = Field(
        default="customer", description="El ROLE es obligatorio")
