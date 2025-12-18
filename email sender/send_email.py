import smtplib, ssl, os
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import credentials

def create_image_attachment(path: str) -> MIMEImage:
    with open(path, "rb") as f:
        image = MIMEImage(f.read())
    return image

def send_email(to_email: str, subject: str, body: str, image: str | None = None):
    host: str = "smtp-mail.outlook.com"
    port: int = 587
    
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP(host, port) as server:
            print("connecting to the server...")
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()

            print("logging in...")
            server.login(credentials.EMAIL, credentials.PASSWORD)
            print("logged in successfully")

            message = MIMEMultipart()
            message["From"] = credentials.EMAIL
            message["To"] = to_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            if image:
                message.attach(create_image_attachment(image))

            print("sending email...")
            server.sendmail(credentials.EMAIL, to_email, message.as_string())
            print("email sent successfully")
    except smtplib.SMTPAuthenticationError as e:
        raise RuntimeError("Authentication failed. Check your email and password.") from e
    
    except smtplib.SMTPConnectError as e:
        raise RuntimeError("Failed to connect to the SMTP server.") from e
    
    except ssl.SSLError as e:
        raise RuntimeError("SSL error occurred during the connection.") from e
    
    except smtplib.SMTPException as e:
        raise RuntimeError("An SMTP error occurred.") from e
def main() -> None:
    try:
        to_email: str = input("Enter recipient email: ")
        if not to_email:
            raise ValueError("Recipient email cannot be empty")
        subject: str = input("Enter subject: ")
        if not subject:
            raise ValueError("Subject cannot be empty")
        body: str = input("Enter email body: ")
        if not body:
            raise ValueError("Email body cannot be empty")
        image: str | None = input("Enter image path (or leave blank): ") or None
        if image and not os.path.isfile(image):
            raise FileNotFoundError(f"Image file at {image} does not exist")
        send_email(to_email, subject, body, image)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
