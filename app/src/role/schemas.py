from pydantic import BaseModel
from pydantic import Field, UUID4


class RoleBase(BaseModel):
    name: str
    code: str

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleInDB(RoleBase):
    id: UUID4 = Field(..., description = "Roles ID")
    class Config:
        orm_mode = True