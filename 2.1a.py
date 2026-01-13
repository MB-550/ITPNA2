import smtplib
from email.mime.text import MIMEText

# SMTP Server Details
smtp_server = "smtp.example.com"
smtp_port = 587
username = "your_email@example.com"
password = "your_password"

# Create Email Message
msg = MIMEText("Hello, this is a test email.")
msg["Subject"] = "Test Email"
msg["From"] = username
msg["To"] = "recipient@example.com"

# Send Email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)
server.sendmail(username, ["recipient@example.com"], msg.as_string())
server.quit()
