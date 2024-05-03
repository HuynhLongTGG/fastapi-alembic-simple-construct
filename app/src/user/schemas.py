from pydantic import BaseModel, EmailStr
from pydantic import Field, UUID4
from datetime import datetime
class UserBase(BaseModel):
    id: UUID4  = Field(..., description = "User ID")
    name: str
    email: EmailStr
    username: str
    password: str
    status: int
    roleId: UUID4  = Field(..., description = "Roles ID")
    createdBy: str
    createdAt: datetime = Field(..., description = "Created At")
    modifiedBy: str
    class Config:
        orm_mode = True
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    username: str
    password: str
    status: int
    roleId: UUID4  = Field(..., description = "Roles ID")
    createdBy: str
    createdAt: datetime = Field(..., description = "Created At")
    modifiedBy: str
    class Config:
        orm_mode = True

class UserRead(UserBase):
    id: UUID4 = Field(..., description = "Roles ID")
    status: bool

    class Config:
        orm_mode = True
