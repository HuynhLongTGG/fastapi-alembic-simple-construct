from sqlalchemy.orm import Session
from .models import User
from .security import get_password_hash, decode_access_token
import uuid
def get_current_user(token: str, db: Session):
    json_decode = decode_access_token(token)
    username = json_decode.get("sub")
    if username is None:
        return None
    return get_user_by_username(db, username)
def get_all_user(db: Session):
    return db.query(User).all()
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
def get_user_by_createdBy(db: Session, createdBy: str):
    return db.query(User).filter(User.createdBy == createdBy).all()
def create_user(db: Session, user):
    db_user = User(
        id=uuid.uuid4(),
        name=user.name,
        email=user.email,
        username=user.username,  # don't hash the username
        password=get_password_hash(user.password),  # hash the password
        status=user.status,
        roleId=user.roleId,
        createdBy=user.createdBy
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def update_user(db: Session, user):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db_user.password = user.password
        db_user.status = user.status
        db_user.roleId = user.roleId
        db_user.createdBy = user.createdBy
        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        return None
def delete_user(db: Session, username: str):
    db_user = get_user_by_username(db, username)
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    else:
        return False
