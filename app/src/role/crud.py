from sqlalchemy.orm import Session
from .models import Role
import uuid
def create_role(db: Session, role):
    db_role = Role(
        id=uuid.uuid4(),
        name=role.name,
        code=role.code,
    )
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def update_role(db: Session, role_id: str, role):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role is None:
        return None
    for key, value in role.dict().items():
        setattr(db_role, key, value)
    db.commit()
    db.refresh(db_role)
    return db_role

def delete_role(db: Session, role_id: str):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role is None:
        return None
    db.delete(db_role)
    db.commit()
    return db_role
def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Role).offset(skip).limit(limit).all()
def get_role_code_by_id(db: Session, role_id: str):
    db_role = db.query(Role).filter(Role.id == role_id).first()
    if db_role is None:
        return None
    return db_role.code