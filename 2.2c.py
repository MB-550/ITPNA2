import imaplib
import email

# IMAP Server Details
imap_server = "imap.gmail.com"
username = "bbggmbab2002@gmail.com"
password = "crnm yedj bgby sjqn"

# Connect to IMAP Server
mail = imaplib.IMAP4_SSL(imap_server)
mail.login(username, password)
mail.select("INBOX")

# Search Unread Emails
status, messages = mail.search(None, 'UNSEEN')
email_ids = messages[0].split()

# Retrieve and Print Email Subjects of the first 20
count = 0
for email_id in email_ids:
    count+=1
    status, msg_data = mail.fetch(email_id, "(RFC822)")
    msg = email.message_from_bytes(msg_data[0][1])
    print(f"Unread Email Subject: {msg['subject']}")
    if count == 20:
        break

# Mark All Unread Emails as Read for the first 20 emails
count = 0
for email_id in email_ids:
    count+=1
    mail.store(email_id, '+FLAGS', '\\Seen')
    print(f"{email_id}: Marked as read")
    if count==20:
        break
mail.logout()
