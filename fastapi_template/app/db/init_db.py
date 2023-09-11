from sqlalchemy.orm import Session

from app import crud, schemas
from app.core.config import settings

def init_db(db: Session) -> None: 
    account = crud.account.get_by_email(db=db, email=settings.FIRST_SUPERUSER)
    if not account:
        account_in = schemas.AccountCreate(
            full_name= "Admin",
            email= settings.FIRST_SUPERUSER,
            password= settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True
        )
        account = crud.account.create(db, obj_in=account_in)