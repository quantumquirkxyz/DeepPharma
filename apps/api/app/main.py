import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from .auth import token_response
from .database import Base, engine, get_db
from .catalog import router as catalog_router
from .datasets import router as datasets_router
from .inventory import router as inventory_router
from .risk import router as risk_router

app = FastAPI(
    title="DeepPharma API",
    version="0.1.0",
    description="Tracer bullet API for inventory and prediction workflows.",
)

allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(inventory_router)
app.include_router(catalog_router)
app.include_router(risk_router)
app.include_router(datasets_router)


@app.post("/token", tags=["auth"])
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db=Depends(get_db),
) -> dict[str, str]:
    return token_response(form_data, db)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "deeppharma-api"}
