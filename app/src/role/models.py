from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text
from core.database import Base
from sqlalchemy.dialects.postgresql import UUID, ARRAY as pg_array
import uuid


class Role(Base):
    __tablename__ = "roles"

    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4())
    name = Column(String)
    code = Column(String)