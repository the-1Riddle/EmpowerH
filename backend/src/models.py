#!/usr/bin/python3
"""
the models
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import relationship

Base = __import__("database").Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    user_email = Column(String, unique=True, index=True)
    user_password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone_number = Column(String)
    age = Column(Integer)
    user_image = Column(String, nullable=True)

    posts = relationship("Post", back_populates="owner", cascade="all, delete")
    blogs = relationship("Blog", back_populates="author", cascade="all, delete")
    comments = relationship("Comment", back_populates="owner", cascade="all, delete")


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    image = Column(String, nullable=True)
    post_desc = Column(Text)
    post_title = Column(String)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), default=func.now())

    owner = relationship("User", back_populates="posts")
    comments = relationship(
        "Comment", back_populates="post", cascade="all, delete-orphan"
    )


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    blog_image = Column(String, nullable=True)
    blog_title = Column(String)
    blog_content = Column(Text)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), default=func.now())

    author = relationship("User", back_populates="blogs")
    comments = relationship(
        "Comment", back_populates="blog", cascade="all, delete-orphan"
    )


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    blog_id = Column(Integer, ForeignKey("blogs.id"))
    comments_data = Column(Text)
    likes = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), default=func.now())

    owner = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
    blog = relationship("Blog", back_populates="comments")
