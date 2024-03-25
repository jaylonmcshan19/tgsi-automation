from simple_salesforce import Salesforce

# Define your Salesforce credentials
#USERNAME = "programmers@thegosolution.com.jaylonm"
#PASSWORD = "Violin##19"
#SECURITY_TOKEN = "XbAmo2VRTxDx3HpKm6mqHtf1"
#CONSUMER_KEY = "3MVG9KshNav2_JdrizuvezzTlzjv11Vy7JV9wX3DUp1ReycdB_ExmcQSUf58SxxTqm.rlnXrTVCFWD.uUlIgE"
#CONSUMER_SECRET = "5747F63AE7EE2E7003CCA19F70EB2E56B9E5AF1CDCB5149D8910433C411BAD1B"

# Initialize Salesforce instance with sandbox login URL
#sf = Salesforce(username=USERNAME, 
 #               password=PASSWORD, 
  #              security_token=SECURITY_TOKEN, 
   #             consumer_key=CONSUMER_KEY,
    #            consumer_secret=CONSUMER_SECRET,
     #           domain='test')

# Simply initializing Salesforce instance will attempt authentication
# If no exception is raised, authentication is successful
#print("Authentication successful!")
# Import necessary libraries
from simple_salesforce import Salesforce
import os

# Salesforce credentials
USERNAME = "programmers@thegosolution.com.jaylonm"
PASSWORD = "Violin##19"
SECURITY_TOKEN = "XbAmo2VRTxDx3HpKm6mqHtf1"
CONSUMER_KEY = "3MVG9KshNav2_JdrizuvezzTlzjv11Vy7JV9wX3DUp1ReycdB_ExmcQSUf58SxxTqm.rlnXrTVCFWD.uUlIgE"
CONSUMER_SECRET = "5747F63AE7EE2E7003CCA19F70EB2E56B9E5AF1CDCB5149D8910433C411BAD1B"

# Authenticate with Salesforce
sf = Salesforce(
    username=USERNAME,
    password=PASSWORD,
    security_token=SECURITY_TOKEN,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    domain='test'  # Change to your Salesforce domain if not using a sandbox
)

# Retrieve metadata components
metadata_components = sf.query("SELECT Id, DeveloperName FROM AuraDefinitionBundle")

# Define the components you want to retrieve source code for
components_to_retrieve = ['TGSI_Customer_Form', 'TGSI_Rater_Auto']

# Directory to save the log file
log_directory = os.path.join(os.path.expanduser('~'), 'Desktop')
log_file_path = os.path.join(log_directory, 'source_code_log.txt')

# Iterate over metadata components and write source code to log file
with open(log_file_path, 'w') as log_file:
    for component in metadata_components['records']:
        component_name = component['DeveloperName']
        if component_name in components_to_retrieve:
            # Retrieve the component's source from Salesforce
            component_metadata = sf.query(f"SELECT Id, Source FROM AuraDefinition WHERE AuraDefinitionBundleId = '{component['Id']}'")
            source_code = component_metadata['records'][0]['Source']
            # Write the source code to the log file
            log_file.write(f"Source code for {component_name}:\n")
            log_file.write(source_code + '\n\n')

print(f"Source code log file saved to {log_file_path}")
