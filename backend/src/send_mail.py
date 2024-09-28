#!/usr/bin/python3
"""
This file contains the code to send emails using FastAPI and FastMail
"""
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import load_dotenv
import os

EmailSchema = __import__("schemas").EmailSchema
PasswordReset = __import__("schemas").PasswordReset


load_dotenv(".env")

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_FROM_NAME=os.getenv("MAIL_FROM_NAME"),
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)


# Function to send contact email
async def contact(email_data: EmailSchema):
    message = MessageSchema(
        subject=f"New Contact Form Submission: {email_data.subject}",
        recipients=[os.getenv("MAIL_USERNAME")],
        body=f"""
        Full Name: {email_data.full_name}<br>
        Email: {email_data.email}<br>
        Phone Number: {email_data.phone_number}<br>
        Message: {email_data.message}
        """,
        subtype="html",
    )
    fm = FastMail(conf)
    await fm.send_message(message)


# Function to send password reset email
async def send_password_reset(email_data: PasswordReset):
    message = MessageSchema(
        subject="Reset Your Password",
        recipients=[email_data.email],
        body=f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Reset Your Password</title>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; }}
                .container {{ width: 100%; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #ffffff; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                .header {{ text-align: center; padding: 20px 0; }}
                .header img {{ width: 100px; }}
                .content {{ padding: 20px; text-align: center; }}
                .button {{ display: inline-block; margin-top: 20px; padding: 10px 20px; background-color: #4CAF50; color: #ffffff; text-decoration: none; border-radius: 5px; }}
                .footer {{ margin-top: 30px; font-size: 12px; color: #777777; text-align: center; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <img src="we-still-dont have a logo lol" alt="EmpowerHer">
                </div>
                <div class="content">
                    <h1>Reset Your Password</h1>
                    <p>Hello,</p>
                    <p>We received a request to reset your password. Click the button below to reset it.</p>
                    <a href="{email_data.reset_link}" class="button">Reset Password</a>
                    <p>If you did not request a password reset, please ignore this email.</p>
                </div>
                <div class="footer">
                    <p>If you have any questions, feel free to contact our support team.</p>
                    <p>Copyright &copy; 2024 EmpowerHer. All rights reserved.</p>
                </div>
            </div>
        </body>
        </html>
        """,
        subtype="html",
    )
    fm = FastMail(conf)
    await fm.send_message(message)
