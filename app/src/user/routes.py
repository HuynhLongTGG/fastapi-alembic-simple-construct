from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import UserCreate, UserRead, UserBase
from .crud import get_user_by_username, create_user, get_current_user, get_user_by_createdBy, get_all_user
from .security import verify_password, create_access_token, decode_access_token
from core.database import get_db
import json
from src.role.crud import get_role_code_by_id
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

@router.post("/signup_adm", response_model=UserCreate, status_code=status.HTTP_201_CREATED)
def user_signup_adm(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_username(db, username=user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)
@router.post("/signup", response_model=UserCreate, status_code=status.HTTP_201_CREATED)
def user_signup_adm(user: UserCreate,token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    json_decode = decode_access_token(token)
    user_id = json_decode.get('user_id')
    user.createdBy = user_id
    if get_user_by_username(db, username=user.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)
@router.post("/login", response_model=dict)
def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db, username=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = create_access_token(data={"user_id": str(user.id),"user_name": user.username, "role_code": get_role_code_by_id(db, user.roleId)})
    return {"access_token": access_token, "token_type": "bearer"}
@router.get("/users", response_model=list[UserBase])
async def read_users(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    json_decode = decode_access_token(token)
    role_code = json_decode.get('role_code')
    if role_code == 'super-admin':
        # If the user is a super-admin, return all users
        return get_all_user(db)
    else:
        # Otherwise, return the users created by the current user
        user_id = json_decode.get('user_id')
        return get_user_by_createdBy(db, user_id)
@router.get("/user/me", response_model=UserBase)
async def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user = get_current_user(token,db)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid token or user not found")
    return UserBase(**user.__dict__)