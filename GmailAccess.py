import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, from_email, to_emails, smtp_server, smtp_port, smtp_username, smtp_password):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject

    # Attach message
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        # Login to the SMTP server
        server.login(smtp_username, smtp_password)
        # Send email
        server.sendmail(from_email, to_emails, msg.as_string())
        # Close the connection
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    subject = "Test Email"
    message = "This is a test email sent from Python."
    from_email = "mayura.testacc@gmail.com"
    to_emails = ["jmmayurahansa@gmail.com", "mayurajayasinghe1mudiyanselage@gmail.com"]
    smtp_server = "smtp-relay.brevo.com"
    smtp_port = 587  # Port for TLS
    smtp_username = "mayura.testacc@gmail.com"
    smtp_password = "xkcOCfdjswP1rKA3"
    
    send_email(subject, message, from_email, to_emails, smtp_server, smtp_port, smtp_username, smtp_password)
