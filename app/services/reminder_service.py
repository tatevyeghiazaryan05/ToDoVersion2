import time
from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from database import SessionLocal
from models import Todo, Users
from services.email_service import send_verification_email, generate_verification_code

import threading


def start_reminder_loop():
    thread = threading.Thread(target=check_reminders, daemon=True)
    thread.start()


def check_verification_deadlines():
    """Check for users approaching or past verification deadline"""
    db: Session = SessionLocal()
    now = datetime.now()
    
    try:
        # Find unverified users
        unverified_users = db.query(Users).filter(
            Users.verified == False
        ).all()
        
        for user in unverified_users:
            if user.created_at:
                deadline = user.created_at + timedelta(days=3)
                days_until_deadline = (deadline - now).days
                
                # Send reminder if within 1 day of deadline or past deadline
                if days_until_deadline <= 1:
                    try:
                        # Generate new verification code
                        code = generate_verification_code()
                        
                        # Send reminder email
                        email_sent = send_verification_email(user.email, code, is_reminder=True)
                        
                        if email_sent:
                            print(f"🔔 Verification reminder sent to {user.email} (days until deadline: {days_until_deadline})")
                        else:
                            print(f"❌ Failed to send verification reminder to {user.email}")
                            
                    except Exception as e:
                        print(f"❌ Error sending verification reminder to {user.email}: {e}")
                        
    except Exception as e:
        print(f"❌ Error checking verification deadlines: {e}")
    finally:
        db.close()


def check_reminders():
    while True:
        db: Session = SessionLocal()
        now = datetime.now()

        try:
            # Check verification deadlines
            check_verification_deadlines()
            
            # Check todo reminders (existing functionality)
            tasks = db.query(Todo).filter(
                Todo.archived == None,
                Todo.status == None,
                Todo.due_date != None
            ).all()

            for task in tasks:
                time_left = task.due_date - now.date()

                if timedelta(days=0) <= time_left <= timedelta(days=1):
                    user = db.query(Users).filter_by(id=task.user_id).first()
                    if user and user.email:
                        message = (
                            f"🔔 Reminder\n\n"
                            f"Dear {user.name},\n"
                            f"Your task '{task.title}' is due on {task.due_date}.\n"
                            f"Please don't forget to complete it on time."
                        )
                        send_verification_email(user.email, message)
                        print(f"✅ Reminder sent to {user.email} for task '{task.title}'")

        except Exception as e:
            print(f"❌ Error: {e}")

        finally:
            db.close()

        print("⏳ Waiting 2 hours for next check...")
        time.sleep(7200)  # 2 hours
