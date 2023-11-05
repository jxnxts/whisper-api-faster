from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
import datetime

class CpfRequest(BaseModel):
    cpf: str = Field(None, title="cpf")