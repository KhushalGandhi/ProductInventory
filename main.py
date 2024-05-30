from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import products

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(products.router)
