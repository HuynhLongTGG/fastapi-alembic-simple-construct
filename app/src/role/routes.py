from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import crud, schemas
from core.database import get_db
router = APIRouter()

@router.get("/roles/", response_model=list[schemas.RoleInDB])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = crud.get_roles(db, skip=skip, limit=limit)
    return roles
@router.post("/roles/", response_model=schemas.RoleInDB)
def create_role(role: schemas.RoleCreate, db: Session = Depends(get_db)):
    return crud.create_role(db, role)

@router.put("/roles/{role_id}", response_model=schemas.RoleInDB)
def update_role(role_id: str, role: schemas.RoleUpdate, db: Session = Depends(get_db)):
    db_role = crud.update_role(db, role_id, role)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.delete("/roles/{role_id}", response_model=schemas.RoleInDB)
def delete_role(role_id: str, db: Session = Depends(get_db)):
    db_role = crud.delete_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role