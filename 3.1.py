import requests
import smtplib
from email.mime.text import MIMEText

# Server Configuration
DATA_SOURCE_URL = "http://localhost:1235/InFlightInfo"  # Replace with actual API URL
SAFETY_LIMITS = {
    "Altitude": (30000, 40000),  # Min and max safe altitude in feet
    "Speed": (200, 600),  # Min and max safe speed in knots
    "Temperature": (0, 50),  # Safe temperature range in Celsius
}

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "bbggmbab2002@gmail.com"
EMAIL_PASSWORD = "crnm yedj bgby sjqn"
EMAIL_RECEIVER = "mak.bhik@gmail.com"

def fetch_flight_data():
    """Retrieve in-flight event data from the server."""
    try:
        response = requests.get(DATA_SOURCE_URL, timeout=10)
        response.raise_for_status()
        return response.json()  # Assuming the API returns JSON data
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def check_safety_margins(data):
    """Check if flight parameters are within safety margins."""
    violations = []
    for param, (min_val, max_val) in SAFETY_LIMITS.items():
        data1 = dict(data[0])
        
        if param in data1:
            value = int(data1[param])
            
            if value < min_val or value > max_val:
                violations.append(f"{param} ({value}) is outside safe range ({min_val}-{max_val})")
                
    return violations

def send_alert(violations):
    """Send an email alert if safety margins are violated."""
    message = MIMEText(f"Safety Alert!\n\nThe following flight parameters are out of range:\n\n" + "\n".join(violations))
    message["Subject"] = "In-Flight Safety Alert"
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())
        server.quit()
        print("Alert email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

def main():
    """Main function to monitor flight data and trigger alerts."""
    data = fetch_flight_data()
    if data:
        violations = check_safety_margins(data)
        
        if violations:
            print(violations)
            send_alert(violations)
        else:
            print("All flight parameters are within safe margins.")



main()

