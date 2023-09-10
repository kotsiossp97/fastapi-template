from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic.networks import EmailStr
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings


router = APIRouter()

@router.get("/", response_model=List[schemas.Account])
def get_accounts(
    db: Session = Depends(deps.get_db),
    current_account: models.Accounts = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve all accounts
    """
    
    accounts = crud.account.get_multi(db)
    return accounts


@router.post("/", response_model=schemas.Account)
def create_account(
    *,
    db: Session = Depends(deps.get_db),
    account_in: schemas.AccountCreate,
    current_account: models.Accounts = Depends(deps.get_current_active_superuser)
) -> Any:
    account = crud.account.get_by_email(db, email=account_in.email)
    if account:
        raise HTTPException(
            status_code=400,
            detail="An account with this email exists in the system."
        )
        
    account = crud.account.create(db, obj_in=account_in)
    
    return account

@router.post("/update/{account_id}", response_model=schemas.Account)
def update_account(
    *,
    db: Session = Depends(deps.get_db),
    account_id: int,
    account_in: schemas.AccountUpdate,
    current_account: models.Accounts = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Update an account.
    """
    account = crud.account.get(db, id=account_id)
    if not account:
        raise HTTPException(
            status_code=404,
            detail="This account does not exist in the system"
        )
    account = crud.account.update(db, db_obj=account, obj_in=account_in)
    return account

@router.delete("/{account_id}", response_model=schemas.Account)
def delete_account(
    *,
    db: Session = Depends(deps.get_db),
    account_id: int,
    current_account: models.Accounts = Depends(deps.get_current_active_superuser)
) -> Any:
    """
    Delete account with given id.
    """
    account = crud.account.get(db=db, id= account_id)
    if not account:
        raise HTTPException(
            status_code=404,
            detail="This account was not found in the system."
        )
    if account.id == current_account.id:
        raise HTTPException(
            status_code=400,
            detail="You cannot delete an account with super priviledges."
        )
    
    account = crud.account.remove(db=db, id=account_id)
    return account

# Calls for getting accounts's self account details
@router.get("/me", response_model=schemas.Account)
def get_account_me(
    db: Session = Depends(deps.get_db),
    current_account: models.Accounts = Depends(deps.get_current_active_account)
) -> Any:
    """
    Retrieve information for logged in account.
    """
    return current_account

@router.post("/me/update", response_model=schemas.Account)
def update_account_me(
    *,
    db: Session = Depends(deps.get_db),
    account_in : schemas.AccountUpdateMe,
    current_account: models.Accounts = Depends(deps.get_current_active_account)
) -> Any:
    """
    Update own account
    """
    account = crud.account.update(db=db, db_obj=current_account, obj_in=account_in)
    return account

@router.delete("/me/", response_model=schemas.Account)
def delete_account_me(
    *,
    db: Session = Depends(deps.get_db),
    current_account: models.Accounts = Depends(deps.get_current_active_account)
) -> Any:
    """
    Delete logged in account
    """
    if crud.account.is_superuser(current_account):
        raise HTTPException(
            status_code=400,
            detail="You cannot delete an account with super priviledges."
        )
    account = crud.account.remove(db=db, id=current_account.id)
    
    return account