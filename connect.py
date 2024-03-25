from selenium import webdriver

# Replace with your own login credentials
username = "your_username"
password = "your_password"

# Open Chrome browser
driver = webdriver.Chrome()

# Navigate to VIT WiFi login page
driver.get("http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.gstatic.com/generate_204")

# Find the username and password input fields
username_field = driver.find_element_by_name("user_name")
password_field = driver.find_element_by_name("user_password")

# Enter your username and password
username_field.send_keys(username)
password_field.send_keys(password)

# Find the login button and click it
login_button = driver.find_element_by_id("login_button")
login_button.click()

# Wait for a few seconds to ensure that login is complete
import time
time.sleep(5)

# Close the browser
driver.quit()