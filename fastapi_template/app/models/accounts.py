from typing import TYPE_CHECKING
from app.db.base_class import Base
from sqlalchemy import Column, Boolean, Integer, String, Enum, Float, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Accounts(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), index=True)
    email = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(50), nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    date_added = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())