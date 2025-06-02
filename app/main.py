from fastapi import FastAPI
from app.api import auth, secure
from app.db.session import engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(secure.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Aether API!"}
