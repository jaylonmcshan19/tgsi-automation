from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
 
# Initialize Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
# Initialize WebDriver
driver = webdriver.Chrome(options=options)
 
try:
    # Navigate to the Real Comp Website
    driver.get("https://infosearch.real-comp.com/ash/faces/protected/databaseSelect.jsp")
 
    # Find username and password input fields
    username_input = driver.find_element(By.NAME, "j_username")
    password_input = driver.find_element(By.NAME, "j_password")
 
    # Input username and password
    username_input.send_keys("TGSInsurance")
    password_input.send_keys("Pytxo$1003295")
 
    # Submit the form
    password_input.submit()
 
    # Wait for the image to be clickable
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td/a/img")))
 
    # Find and click on the image using the provided XPath
    image = driver.find_element(By.XPATH, "/html/body/form/div[1]/table/tbody/tr/td/table/tbody/tr[4]/td/a/img")
    image.click()
 
    # You can add further actions here if needed
 
except Exception as e:
    print("An error occurred:", e)
