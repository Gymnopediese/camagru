import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

from services.app import app
import os
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = os.environ.get('EMAIL_SENDER')
app.config["MAIL_PASSWORD"] = os.environ.get('EMAIL_PASSWORD')
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get('EMAIL_SENDER')


mail = Mail(app)

s = URLSafeTimedSerializer(app.config["SECRET_KEY"])

def generate_confirmation_token(email):
    return s.dumps(email, salt="email-confirm")

def confirm_token(token, expiration=3600):
    try:
        email = s.loads(token, salt="email-confirm", max_age=expiration)
    except:
        return False
    return email


mail_server = None

def get_mail_server():
    
    global mail_server
    
    if mail_server:
        return mail_server
        
    
    email_sender = os.environ.get('EMAIL_SENDER')
    email_password = os.environ.get('EMAIL_PASSWORD')


    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.starttls()
    mail_server.login(email_sender, email_password)
    
    return mail_server

    

@app.route('/send_mail')
def send_mail():
    sender_email = os.environ.get('EMAIL_SENDER')
    receiver_email = "kalityoflife@gmail.com"

    server =  get_mail_server()
    
    message = MIMEText('Hello, this is a test email')
    message['Subject'] = 'Test email'
    message['From'] = sender_email
    message['To'] = receiver_email
    
    server.sendmail(sender_email, receiver_email, message.as_string())

    return "Mail sent"