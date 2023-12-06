from os import access
from fastapi import APIRouter, Depends, status, HTTPException, Response
import models
from sqlalchemy.orm import Session
from database import get_db
from schemas import UserLogin
from utils import hash_password, verify
import oauth2


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", status_code=status.HTTP_200_OK)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    query = db.query(models.User).where(models.User.email == user_credentials.email)
    user = query.first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Invalid credentials",
        )
    if not verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Password is not correct"
        )

    access_token = oauth2.create_access_token(data={"user_id": user.id})
    return {"token": access_token, "token_type": "bearer"}
