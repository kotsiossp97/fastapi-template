from typing import Optional

from pydantic import BaseModel, EmailStr
from datetime import datetime

# Shared properties
class AccountBase(BaseModel):
    email: EmailStr = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None
    date_added: Optional[datetime]
    date_updated: Optional[datetime]

# Properties to receive via API on creation
class AccountCreate(AccountBase):
    email: EmailStr
    password: str
    
# Properties to receive via API on update
class AccountUpdate(AccountBase):
    password: Optional[str] = None


class AccountUpdateMe(BaseModel):
    email: Optional[EmailStr]   = None
    password: Optional[str]     = None
    full_name: Optional[str]    = None

class AccountInDBBase(AccountBase):
    id: int
    
    class Config:
        orm_mode = True
    
# Additional properties to return via API
class Account(AccountInDBBase):
    pass


# Additional properties stored in DB
class AccountInDB(AccountInDBBase):
    pass
