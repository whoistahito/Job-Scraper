from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from credential import Credential


def send_email(body, receiver_email, is_html=True):
    cred = Credential()
    # Email configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = cred.get_email_address()
    password = cred.get_email_password()

    # Create the email content
    subject = "Test Email"

    # Set up the MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    if is_html:
        message.attach(MIMEText(body, "html"))
    else:
        message.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the connection to the SMTP server
        server.quit()

