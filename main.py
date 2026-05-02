# Import Selenium WebDriver to control the browser
from selenium import webdriver

# Import By class to locate elements on the webpage
from selenium.webdriver.common.by import By

# ===================== SETUP CHROME OPTIONS =====================

# Create Chrome options object
chrome_options = webdriver.ChromeOptions()

# Keep Chrome browser open even after script execution ends
chrome_options.add_experimental_option("detach", True)

# ===================== INITIALIZE DRIVER =====================

# Launch Chrome browser with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the target website (Python official website)
driver.get("https://www.python.org/")

# ===================== (COMMENTED) AMAZON PRICE SCRAPER =====================

# Example code for scraping price from Amazon (currently not used)

# price_rupee = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_paisa = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_rupee.text}.{price_paisa.text}")

# ===================== SCRAPE UPCOMING EVENTS =====================

# Find all event time elements using CSS selector
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")

# Find all event name elements using CSS selector
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# Create an empty dictionary to store events
events = {}

# Loop through all extracted events
for n in range(len(event_times)):
    # Store each event as a dictionary inside 'events'
    events[n] = {
        "time": event_times[n].text,   # Extract event date/time
        "name": event_names[n].text    # Extract event title
    }

# Print the final dictionary of events
print(events)

# ===================== CLOSE BROWSER =====================

# Close current browser tab (optional, currently commented)
# driver.close()

# Quit the entire browser session
driver.quit()