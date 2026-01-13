import poplib
from email.parser import BytesParser

try:
    # POP3 Server Details
    pop3_server = "pop.gmail.com"
    username = "bbggmbab2002@gmail.com"
    password = "crnm yedj bgby sjqn"
    
    # Connect to POP3 Server
    server = poplib.POP3_SSL(pop3_server)
    server.user(username)
    server.pass_(password)
    
    # List Messages
    num_messages = len(server.list()[1])
    print(f"Total messages: {num_messages}")
    
    # Retrieve and Print Email Subjects
    for i in range(num_messages):
        raw_email = b"\n".join(server.retr(i + 1)[1])
        msg = BytesParser().parsebytes(raw_email)
        print(f"Email {i+1} Subject: {msg['subject']}")

# Delete First Email (example)

    server.dele(1)
    print("message deleted")
    
except Exception as e:
    print(e)
    
finally:    
    server.quit()
