#!/usr/bin/python3
"""
pydantic schemes
"""
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import List, Optional
from datetime import datetime


class UserBase(BaseModel):
    user_name: str
    user_email: EmailStr
    first_name: str
    last_name: str
    phone_number: str
    age: int
    user_image: Optional[str] = None


class UserCreate(UserBase):
    user_password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class PostBase(BaseModel):
    post_title: str
    post_desc: str
    image: Optional[str] = None
    likes: Optional[int] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class BlogBase(BaseModel):
    blog_title: str
    blog_content: str
    blog_image: Optional[str] = None
    likes: Optional[int] = None


class BlogCreate(BlogBase):
    pass


class Blog(BlogBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class CommentBase(BaseModel):
    comments_data: str
    likes: Optional[int] = None


class CommentCreate(CommentBase):
    post_id: Optional[int] = None
    blog_id: Optional[int] = None


class Comment(CommentBase):
    id: int
    user_id: int
    post_id: Optional[int] = None
    blog_id: Optional[int] = None
    created_at: datetime

    class Config:
        from_attributes = True


# Adding token-related schemas
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_email: Optional[str] = None


class ResetPassword(BaseModel):
    reset_password_token: str


class PasswordResetRequest(BaseModel):
    email: str


class PasswordReset(BaseModel):
    email: EmailStr
    reset_link: str


class PasswordUpdate(BaseModel):
    email: str
    old_password: str
    new_password: str


class EmailSchema(BaseModel):
    email: EmailStr
    full_name: str
    subject: str
    phone_number: str
    message: str
