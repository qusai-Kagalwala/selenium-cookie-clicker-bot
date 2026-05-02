# Import Selenium WebDriver to control the browser
from selenium import webdriver

# Import By class to locate elements on the webpage
from selenium.webdriver.common.by import By

# Import Keys (not used here but useful for keyboard actions)
from selenium.webdriver.common.keys import Keys

# ===================== SETUP CHROME OPTIONS =====================

# Create Chrome options object
chrome_options = webdriver.ChromeOptions()

# Keep Chrome browser open after script execution ends
chrome_options.add_experimental_option("detach", True)

# ===================== INITIALIZE DRIVER =====================

# Launch Chrome browser with specified options
driver = webdriver.Chrome(options=chrome_options)

# Maximize the browser window for better visibility
driver.maximize_window()

# Open the signup page
driver.get("https://secure-retreat-92358.herokuapp.com/")

# ===================== LOCATE INPUT FIELDS =====================

# Find the first name input field using its 'name' attribute
first_name = driver.find_element(By.NAME, value="fName")

# Find the last name input field using its 'name' attribute
last_name = driver.find_element(By.NAME, value="lName")

# Find the email input field using its 'name' attribute
email = driver.find_element(By.NAME, value="email")

# ===================== FILL FORM DATA =====================

# Enter first name into the input field
first_name.send_keys("Qusai")

# Enter last name into the input field
last_name.send_keys("Kagalwala")

# Enter email into the input field
email.send_keys("qusaikagal1@email.com")

# ===================== SUBMIT FORM =====================

# Locate the submit button using CSS selector
submit = driver.find_element(By.CSS_SELECTOR, value="form button")

# Click the submit button to send the form
submit.click()

# ===================== OPTIONAL CLEANUP =====================

# driver.close()   # Closes current tab
# driver.quit()    # Closes entire browser session