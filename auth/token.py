from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from dotenv import load_dotenv
import os


load_dotenv()

security = HTTPBearer()

valid_token = os.getenv("VALID_TOKEN")

async def authenticate_token(token: str = Depends(security)):

    token = token.credentials

    if not token or token != valid_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    return token