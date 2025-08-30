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


def send_verification_email(user_email, is_reminder=False):
    """Send verification code to user email with a clickable button"""
    url = f"http://127.0.0.1:8000/ToDo/api/user/auth/verify/{user_email}"

    if is_reminder:
        subject = "🔔 Verification Reminder - Complete Your Account Setup"
        html_content = f"""
        <html>
          <body>
            <p>Hello!</p>
            <p>This is a reminder that your account verification is still pending.</p>
            <p>
              <a href="{url}" style="
                  display:inline-block;
                  padding:10px 20px;
                  font-size:16px;
                  color:#ffffff;
                  background-color:#28a745;
                  text-decoration:none;
                  border-radius:5px;">
                ✅ Verify My Account
              </a>
            </p>
            <p>Please verify your account within 3 days to avoid account restrictions.</p>
            <p>If you have any questions, please contact support.</p>
            <p>Best regards,<br>Todo App Team</p>
          </body>
        </html>
        """
    else:
        subject = "✅ Verify Your Todo App Account"
        html_content = f"""
        <html>
          <body>
            <p>Welcome to Todo App!</p>
            <p>Thank you for signing up. To complete your account setup, please click the button below:</p>
            <p>
              <a href="{url}" style="
                  display:inline-block;
                  padding:10px 20px;
                  font-size:16px;
                  color:#ffffff;
                  background-color:#007bff;
                  text-decoration:none;
                  border-radius:5px;">
                ✅ Verify My Account
              </a>
            </p>
            <p>Best regards,<br>Todo App Team</p>
          </body>
        </html>
        """

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = user_email
    msg.add_alternative(html_content, subtype="html")  # Send HTML email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
