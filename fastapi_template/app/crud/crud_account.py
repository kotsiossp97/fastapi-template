from typing import List, Any, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.accounts import Accounts
from app.schemas.account import AccountCreate, AccountUpdate


class CRUDAccount(CRUDBase[Accounts, AccountCreate, AccountUpdate]):
    
    def get_by_email(self, db: Session, *, email: str) -> Optional[Accounts]:
        return db.query(Accounts).filter(Accounts.email == email).first()

    def authenticate(self, db:Session, *, email: str, password:str) -> Optional[Accounts]:
        account = self.get_by_email(db, email=email)
        if not account:
            return None
        if not account.password == password:
            return None
        return account
        
    def is_active(self, account: Accounts) -> bool:
        return account.is_active

    def is_superuser(self, account: Accounts) -> bool:
        return account.is_superuser
    
account = CRUDAccount(Accounts)