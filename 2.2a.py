import smtplib
from email.mime.text import MIMEText

# SMTP Server Details
smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "bbggmbab2002@gmail.com"
password = "crnm yedj bgby sjqn"

# Create Email Message
msg = MIMEText("Hello, this is a test email.")
msg["Subject"] = "Test Email"
msg["From"] = username
msg["To"] = "mak.bhik@gmail.com"

# Send Email
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)
server.sendmail(username, ["mak.bhik@gmail.com"], msg.as_string())
server.quit()
