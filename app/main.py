from fastapi import FastAPI
from src.user.routes import router as user_router
from src.role.routes import router as role_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(role_router, tags=["roles"])