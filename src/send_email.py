import smtplib
import ssl
from email.message import EmailMessage

def send_email():
    # Credentials and content
    sender = "tarbabyelvis@gmail.com"
    receiver = "elvischits@yahoo.com"
    password = "csgzyhqfodysvxjs" 
    subject = "Data Protection Training"
    body = "Good day Tarbaby, I hope this email finds you well. I wanted to inform you about the upcoming data protection training starting Friday, 20 March 2026 at Africa University in Mutare. Please let me know if you have any questions or if you need any additional information. Best regards, Fatima Gumbeze"

    # Construct the message
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # Send the email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=context) # Secure connection
            server.login(sender, password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("Sending email...")
    send_email()


if __name__ == "__main__":
    main()