#!/usr/bin/python3
"""
User authentication
"""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from sqlalchemy.orm import Session
import crud
import schemas


# Importing TokenData from schemas
TokenData = __import__("schemas").TokenData
get_db = __import__("database").get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
RESET_MINUTES = 10


class Hash:
    @staticmethod
    def verify_pwd(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def hash_pwd(password):
        return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_email: str = payload.get("sub")
        if user_email is None:
            raise credentials_exception
        token_data = TokenData(user_email=user_email)
    except JWTError:
        raise credentials_exception

    user = crud.get_user_by_email(db, user_email=token_data.user_email)
    if user is None:
        raise credentials_exception
    return user


"""
Password Reset Operations
"""
def create_password_reset_token(email: str):
    expire = datetime.utcnow() + timedelta(minutes=RESET_MINUTES)
    to_encode = {"sub": email, "exp": expire}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password_reset_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload["sub"]
        if not email:
            raise jwt.PyJWTError
        return email
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def reset_password(db: Session, email: str, new_password: str):
    user = get_user_by_email(db, email)
    if user:
        hashed_password = pwd_context.hash(new_password)
        user.user_password = hashed_password
        db.commit()
        db.refresh(user)
        return user
    else:
        return None