#!/usr/bin/env python3
"""
Main app: where all parts created are implemented
"""
from fastapi import (
    Depends,
    FastAPI,
    HTTPException,
    status,
    File,
    Form,
    UploadFile,
    BackgroundTasks,
)
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import EmailStr
import os
import logging
from sqlalchemy.orm import Session
from typing import List

import crud
import models
from schemas import EmailSchema
import schemas
from auth import (
    Hash,
    create_access_token,
    get_current_user,
    verify_password_reset_token,
    reset_password,
    create_password_reset_token
)
from database import SessionLocal, engine, get_db
from send_mail import contact, send_password_reset

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Added CORS Middleware
origins = ["http://localhost:3000", "https://empowerherr.tech"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PICTURES_DIR = os.path.join(BASE_DIR, "static/Pictures")
os.makedirs(PICTURES_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")


# User Routes
@app.post("/api/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user.user_email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered"
        )
    hashed_password = Hash.hash_pwd(user.user_password)
    user.user_password = hashed_password
    return crud.create_user(db=db, user=user)


@app.get("/api/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/api/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return db_user


@app.get("/api/users/email/{user_email}", response_model=schemas.User)
def read_user_by_email(user_email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, user_email=user_email)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return db_user


# +++++++++++++++++++++Post Routes
@app.post("/api/posts/", response_model=schemas.Post)
def create_post(
    post_title: str = Form(...),
    post_desc: str = Form(...),
    user_id: int = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db),
):
    logging.info(f"Received post_title: {post_title}")
    logging.info(f"Received post_desc: {post_desc}")
    logging.info(f"Received user_id: {user_id}")
    logging.info(f"Received image: {image.filename if image else 'No image uploaded'}")

    image_name = None
    if image:
        image_name = image.filename
        image_path = os.path.join(PICTURES_DIR, image_name)
        with open(image_path, "wb") as f:
            f.write(image.file.read())

    post_data = schemas.PostCreate(
        post_title=post_title, post_desc=post_desc, image=image_name
    )

    new_post = crud.create_post(db=db, post=post_data, user_id=user_id)
    return new_post


@app.get("/api/posts/", response_model=List[schemas.Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts


@app.get("/api/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return db_post


@app.delete("/api/posts/{post_id}", response_model=schemas.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    return crud.delete_post(db=db, post_id=post_id)


# +++++++++++++++++++Blog Routes
@app.post("/api/blogs/", response_model=schemas.Blog)
def create_post(
    blog_title: str = Form(...),
    blog_content: str = Form(...),
    user_id: int = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db),
):
    logging.info(f"Received blog_title: {blog_title}")
    logging.info(f"Received blog_content: {blog_content}")
    logging.info(f"Received user_id: {user_id}")
    logging.info(f"Received image: {image.filename if image else 'No image uploaded'}")

    image_name = None
    if image:
        image_name = image.filename
        image_path = os.path.join(PICTURES_DIR, image_name)
        with open(image_path, "wb") as f:
            f.write(image.file.read())

    blog_data = schemas.BlogCreate(
        blog_title=blog_title, blog_content=blog_content, image=image_name
    )

    new_blog = crud.create_blog(db=db, blog=blog_data, user_id=user_id)
    return new_blog


@app.get("/api/blogs/", response_model=List[schemas.Blog])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db, skip=skip, limit=limit)
    return blogs


@app.get("/api/blogs/{blog_id}", response_model=schemas.Blog)
def read_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="blog not found"
        )
    return db_blog


@app.get("/api/blogs/likes", response_model=List[schemas.Blog])
def read_blogs_by_likes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    blogs = crud.get_blog_likes(db, skip=skip, limit=limit)
    return blogs


@app.patch("/api/blogs/add-likes", response_model=schemas.Blog)
def add_blog_likes(blog_id: int, db: Session = Depends(get_db)):
    blog = crud.increment_blog_likes(db, blog_id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog


@app.delete("/api/blogs/{blog_id}", response_model=schemas.Blog)
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="blog not found"
        )
    return crud.delete_blog(db=db, blog_id=post_id)


# Comment Routes
@app.post("/api/comments/", response_model=schemas.Comment)
def create_comment(
    comment: schemas.CommentCreate, user_id: int, db: Session = Depends(get_db)
):
    print(f"Received request to create comment: {comment} by user {user_id}")
    new_comment = crud.create_comment(db=db, comment=comment, user_id=user_id)
    print(f"Comment created successfully: {new_comment}")
    return new_comment


@app.get("/api/comments/", response_model=List[schemas.Comment])
def read_comments(
    post_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    comments = crud.get_comments_by_post(db, post_id=post_id, skip=skip, limit=limit)
    return comments


@app.get("/api/comments/{comment_id}", response_model=schemas.Comment)
def read_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found"
        )
    return db_comment


@app.patch("/api/comment/add-likes", response_model=schemas.Comment)
def add_comment_likes(comment_id: int, db: Session = Depends(get_db)):
    comment = crud.increment_comment_likes(db, comment_id)
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    return comment


@app.delete("/api/comments/{comment_id}", response_model=schemas.Comment)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    db_comment = crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found"
        )
    return crud.delete_comment(db=db, comment_id=comment_id)


# Authentication Routes
@app.post("/token", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.user_email})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/api/users/me/", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):
    return current_user


# Password Reset Routes
@app.post("/api/password-reset-request")
async def password_reset_request(
    request: schemas.PasswordReset, db: Session = Depends(get_db)
):
    user = crud.get_user_by_email(db, request.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    reset_token = create_access_token(data={"sub": user.user_email})
    reset_link = f"https://empowerherr.tech/reset-password?token={reset_token}"

    email_data = schemas.PasswordReset(email=user.user_email, reset_link=reset_link)
    await send_password_reset(email_data)

    return {"message": "Password reset email sent"}


# Am route to reset the password using the token
@app.put("/api/reset-password")
async def reset_password(token: str, new_password: str, db: Session = Depends(get_db)):
    email = verify_password_reset_token(token)
    if email is None:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    user = crud.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = Hash.hash_pwd(new_password)
    user.user_password = hashed_password
    db.commit()
    db.refresh(user)

    return {"message": "Password reset successful"}


@app.post("/api/password-update")
def password_reset(
    password_update: schemas.PasswordUpdate, db: Session = Depends(get_db)
):
    user = crud.get_user_by_email(db, password_update.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if not Hash.verify_pwd(password_update.old_password, user.user_password):
        raise HTTPException(status_code=401, detail="Old password is incorrect")

    hashed_password = Hash.hash_pwd(password_update.new_password)
    user.user_password = hashed_password
    db.commit()
    db.refresh(user)
    return {"message": "Password reset successful"}


# Contact Form Route
@app.post("/api/contact-mail/")
async def send_contact_email(
    background_tasks: BackgroundTasks,
    email: EmailStr = Form(...),
    full_name: str = Form(...),
    subject: str = Form(...),
    phone_number: str = Form(...),
    message: str = Form(...),
):
    email_data = EmailSchema(
        email=email,
        full_name=full_name,
        subject=subject,
        phone_number=phone_number,
        message=message,
    )
    background_tasks.add_task(contact, email_data)
    return JSONResponse(status_code=200, content={"message": "Email has been sent"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
