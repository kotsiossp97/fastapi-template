from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core import security
from app.core.config import settings
router = APIRouter()


@router.post("/access-token", response_model=schemas.Token)
def login_access_token(
    db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    account = crud.account.authenticate(
        db, email=form_data.username, password=form_data.password
    )
    if not account:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    elif not crud.account.is_active(account):
        raise HTTPException(status_code=400, detail="Inactive account")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(
            account.id, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }
    
    
@router.post("/test-token", response_model=schemas.Account)
def test_token(current_account: models.Accounts = Depends(deps.get_current_account)) -> Any:
    """
    Test access token
    """
    return current_account