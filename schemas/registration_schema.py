from pydantic import BaseModel
from typing import Optional


class RegistrationInfo(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    support_type: Optional[str] = None
        