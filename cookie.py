# Import Selenium WebDriver to control the browser
from selenium import webdriver

# Import By to locate elements on the webpage
from selenium.webdriver.common.by import By

# Import exception handling for missing elements
from selenium.common.exceptions import NoSuchElementException

# Import time functions for delays and timers
from time import sleep, time

# ===================== SETUP CHROME DRIVER =====================

# Create Chrome options object
chrome_options = webdriver.ChromeOptions()

# Keep browser open after script finishes
chrome_options.add_experimental_option("detach", True)

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open Cookie Clicker game website
driver.get("https://ozh.github.io/cookieclicker/")

# Wait for initial page load
sleep(3)

# ===================== HANDLE LANGUAGE SELECTION =====================

print("Looking for language selection...")

try:
    # Locate and click English language button
    language_button = driver.find_element(by=By.ID, value="langSelect-EN")
    print("Found language button, clicking...")
    language_button.click()

    # Wait for game to load after language selection
    sleep(3)

except NoSuchElementException:
    # If language selection is not found
    print("Language selection not found")

# Extra wait to ensure everything is fully loaded
sleep(2)

# ===================== GET GAME ELEMENTS =====================

# Locate the main cookie button
cookie = driver.find_element(by=By.ID, value="bigCookie")

# Create list of all store item IDs (product0 → product17)
item_ids = [f"product{i}" for i in range(18)]

# ===================== TIMER SETUP =====================

wait_time = 5  # Check store every 5 seconds

# Timer to trigger purchase check
timeout = time() + wait_time

# Total runtime (5 minutes)
five_min = time() + 60 * 5

# ===================== MAIN GAME LOOP =====================

while True:
    # Continuously click the cookie to generate cookies
    cookie.click()

    # Every 5 seconds, attempt to buy best available upgrade
    if time() > timeout:
        try:
            # Get current cookie count element
            cookies_element = driver.find_element(by=By.ID, value="cookies")

            # Extract numeric value from text (e.g., "1,234 cookies")
            cookie_text = cookies_element.text
            cookie_count = int(cookie_text.split()[0].replace(",", ""))

            # Get all store product elements
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")

            # Find most expensive affordable item
            best_item = None

            # Iterate from most expensive to cheapest
            for product in reversed(products):
                # Check if item is enabled (affordable)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Purchase the best available item
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            # Handle cases where elements or values are not found
            print("Couldn't find cookie count or items")

        # Reset purchase timer
        timeout = time() + wait_time

    # ===================== STOP CONDITION =====================

    # Stop script after 5 minutes
    if time() > five_min:
        try:
            # Print final cookie count
            cookies_element = driver.find_element(by=By.ID, value="cookies")
            print(f"Final result: {cookies_element.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break