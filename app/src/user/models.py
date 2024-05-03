from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from core.database import Base
from sqlalchemy.dialects.postgresql import UUID, ARRAY as pg_array
import datetime
import uuid


class User(Base):
    
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    status = Column(Integer)
    roleId = Column(UUID(as_uuid=True), ForeignKey('roles.id'))
    createdBy = Column(String,default="",nullable=True)
    createdAt = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    modifiedBy = Column(String,default="",nullable=True)