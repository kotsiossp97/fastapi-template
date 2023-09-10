from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from pydantic import ValidationError
from jose import jwt

from app import crud, models, schemas
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def get_current_account(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> models.Accounts:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    account = crud.account.get(db, id=token_data.sub)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account


def get_current_active_account(
    current_account: models.Accounts = Depends(get_current_account),
) -> models.Accounts:
    if not crud.account.is_active(current_account):
        raise HTTPException(status_code=400, detail="Inactive account")
    return current_account


def get_current_active_superuser(
    current_account: models.Accounts = Depends(get_current_account),
) -> models.Accounts:
    if not crud.account.is_superuser(current_account):
        raise HTTPException(
            status_code=400, detail="This account doesn't have enough privileges"
        )
    return current_account
