import os
from datetime import UTC, datetime, timedelta
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, Security, status
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    SecurityScopes,
)
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from .database import get_db
from .models import Usuario

SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY must be configured before starting the API")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/token",
    scopes={
        "inventory:read": "Consultar inventario",
        "inventory:write": "Actualizar inventario",
        "alerts:manage": "Gestionar alertas",
    },
)


def create_access_token(username: str, scopes: list[str]) -> str:
    expires = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(
        {"sub": username, "scope": " ".join(scopes), "exp": expires},
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def authenticate(db: Session, username: str, password: str) -> Usuario | None:
    user = db.query(Usuario).filter_by(username=username, activo=True).one_or_none()
    if user is None or not password_hash.verify(password, user.hashed_password):
        return None
    return user


def get_current_user(
    security_scopes: SecurityScopes,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
) -> Usuario:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        token_scopes = str(payload.get("scope", "")).split()
        if not username or any(
            scope not in token_scopes for scope in security_scopes.scopes
        ):
            raise credentials_exception
    except InvalidTokenError as error:
        raise credentials_exception from error

    user = db.query(Usuario).filter_by(username=username, activo=True).one_or_none()
    if user is None:
        raise credentials_exception
    return user


def require_scope(scope: str):
    def dependency(
        current_user: Annotated[Usuario, Security(get_current_user, scopes=[scope])],
    ) -> Usuario:
        return current_user

    return dependency


def _token_response(user: Usuario) -> dict[str, str]:
    role_scopes = {
        "administrador_sistema": [
            "inventory:read",
            "inventory:write",
            "alerts:manage",
        ],
        "farmaceutico": ["inventory:read", "inventory:write", "alerts:manage"],
        "administrador_farmacia": ["inventory:read", "inventory:write"],
        "ingeniero_ml": ["inventory:read"],
    }
    scopes = role_scopes.get(user.rol, [])
    return {
        "access_token": create_access_token(user.username, scopes),
        "token_type": "bearer",
    }


def token_response(form_data: OAuth2PasswordRequestForm, db: Session) -> dict[str, str]:
    user = authenticate(db, form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return _token_response(user)
