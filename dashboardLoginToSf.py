from simple_salesforce import Salesforce
import schedule
import time
import datetime

# Salesforce credentials
USERNAME = "programmers@thegosolution.com.jaylonm"
PASSWORD = "Violin##19"
SECURITY_TOKEN = "XbAmo2VRTxDx3HpKm6mqHtf1"
CONSUMER_KEY = "3MVG9KshNav2_JdrizuvezzTlzjv11Vy7JV9wX3DUp1ReycdB_ExmcQSUf58SxxTqm.rlnXrTVCFWD.uUlIgE"
CONSUMER_SECRET = "5747F63AE7EE2E7003CCA19F70EB2E56B9E5AF1CDCB5149D8910433C411BAD1B"

# Authenticate with Salesforce
def login_to_salesforce():
    try:
        sf = Salesforce(
            username=USERNAME,
            password=PASSWORD,
            security_token=SECURITY_TOKEN,
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            domain='test'
        )
        print("Successfully logged in to Salesforce at", datetime.datetime.now())
        # Log successful login timestamp to database or data structure
    except Exception as e:
        print("Error logging in to Salesforce:", str(e))

# Schedule login task to run every 5 minutes
schedule.every(5).minutes.do(login_to_salesforce)

# Main loop to run scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
