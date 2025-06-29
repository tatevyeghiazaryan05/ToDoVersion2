from datetime import datetime, timedelta

from fastapi import HTTPException, status

from db_connection import DbConnection
from schemas.user_auth_schemas import UserSignUpSchema, UserLoginSchema, VerificationCodeSchema
from core.security import pwd_context
from services.email_service import send_verification_email, generate_verification_code
from core.security import create_access_token


class UserAuth:
    def __init__(self):
        self.db = DbConnection()

    def signup(self, data: UserSignUpSchema):
        name = data.name
        email = data.email
        password = data.password

        try:
            hashed_password = pwd_context.hash(password)
        except Exception:
            raise HTTPException(status_code=500, detail="Error hashing password")

        try:
            self.db.cursor.execute("""INSERT INTO users 
                                (name,email,password) 
                                VALUES (%s,%s,%s)""",
                                   (name, email, hashed_password))
            self.db.conn.commit()
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail=f"Database Query error :{e} ")

        try:
            self.db.cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
        except Exception:
            raise HTTPException(status_code=500, detail="Database select error")

        try:
            user_row = self.db.cursor.fetchone()
            print(user_row)
        except Exception:
            raise HTTPException(
                                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Fetch error")
        if not user_row:
            raise HTTPException(status_code=404, detail="User ID lookup failed")
        user_id = dict(user_row).get("id")

        code = generate_verification_code()

        try:
            self.db.cursor.execute("""INSERT INTO verificationcode (code, user_id) VALUES (%s, %s)""",
                                   (code, user_id))
            self.db.conn.commit()
        except Exception:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Error inserting verification code")

        try:
            email_sent = send_verification_email(email, code)
            if not email_sent:
                raise HTTPException(status_code=500, detail="Failed to send verification email.")
        except Exception:
            raise HTTPException(status_code=500, detail="Error sending verification email")

    def verify(self, verification_data: VerificationCodeSchema):
        try:
            self.db.cursor.execute("SELECT id FROM users WHERE email = %s", (verification_data.email,))
        except Exception:
            raise HTTPException(status_code=500, detail="Database query error")

        try:
            user = self.db.cursor.fetchone()
        except Exception:
            raise HTTPException(status_code=500, detail="Database fetch error")

        if not user:
            raise HTTPException(status_code=400, detail="User not found.")

        user_id = dict(user).get("id")

        try:
            self.db.cursor.execute("""SELECT * FROM verificationcode 
                                WHERE user_id = %s AND code = %s""",
                                   (user_id, verification_data.code))
        except Exception:
            raise HTTPException(status_code=500, detail="Database query error")

        try:
            data = self.db.cursor.fetchone()
        except Exception:
            raise HTTPException(status_code=500, detail="Database fetch error")

        try:
            if not data:
                raise HTTPException(status_code=400, detail="Invalid verification code.")
        except Exception:
            raise HTTPException(status_code=500, detail="Error fetching verification code")

        created_at = data['created_at']
        expiration_time = created_at + timedelta(minutes=15)
        if datetime.now() > expiration_time:
            try:
                self.db.cursor.execute("DELETE FROM verificationcode WHERE id = %s", (data.get("id"),))
                self.db.conn.commit()
            except Exception:
                raise HTTPException(status_code=500, detail="Error deleting expired code")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Verification code has expired after 15 minutes."
            )

        try:
            self.db.cursor.execute("""UPDATE users SET verified=%s WHERE id=%s""",
                                   ("true", user_id))
            self.db.conn.commit()
        except Exception:
            raise HTTPException(status_code=500, detail="Error updating user as verified")

        try:
            self.db.cursor.execute("DELETE FROM verificationcode WHERE id = %s", (data.get("id"),))
            self.db.conn.commit()
        except Exception:
            raise HTTPException(status_code=500, detail="Error deleting verification code")

    def login(self, login_data: UserLoginSchema):
        email = login_data.email
        password = login_data.password

        try:
            self.db.cursor.execute("""SELECT * FROM users WHERE email = %s""", (email,))
        except Exception:
            raise HTTPException(status_code=500, detail="Database query error")

        try:
            user = self.db.cursor.fetchone()
        except Exception:
            raise HTTPException(status_code=500, detail="Database fetch error")

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found!"
            )

        try:
            user = dict(user)
            user_password_db = user.get("password")
        except Exception:
            raise HTTPException(status_code=500, detail="Error processing user data")

        if not pwd_context.verify(password, user_password_db):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Password is not correct!"
            )

        try:
            user_id_db = user.get("id")
            user_email_db = user.get("email")

            token = create_access_token({"id": user_id_db, "email": user_email_db})
        except Exception:
            raise HTTPException(status_code=500, detail="Token creation error")

        return {"access_token": token}
