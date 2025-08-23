import datetime
import time
import smtplib
from email.message import EmailMessage
import secrets
import string


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "tatevikyeghiazaryann5@gmail.com"
EMAIL_PASSWORD = "klcm ecsh nfcb xhzs"


def generate_verification_code(length=8):
    characters = string.ascii_letters + string.digits
    random_part = ''.join(secrets.choice(characters) for _ in range(length))
    timestamp_part = str(int(datetime.datetime.now().time().microsecond))
    return random_part + timestamp_part


def send_verification_email(user_email, code, is_reminder=False):
    """Send verification code to user email"""
    
    if is_reminder:
        subject = "🔔 Verification Reminder - Complete Your Account Setup"
        content = f"""
Hello!

This is a reminder that your account verification is still pending.

Your verification code is: {code}

Please verify your account within 3 days to avoid account restrictions.

If you have any questions, please contact support.

Best regards,
Todo App Team
        """
    else:
        subject = "✅ Verify Your Todo App Account"
        content = f"""
Welcome to Todo App!

Thank you for signing up. To complete your account setup, please use this verification code:

{code}

This code will expire in 15 minutes.

Best regards,
Todo App Team
        """

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = user_email
    msg.set_content(content.strip())

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
