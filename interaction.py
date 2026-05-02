# Import Selenium WebDriver to control the browser
from selenium import webdriver

# Import By class to locate elements on the webpage
from selenium.webdriver.common.by import By

# Import Keys to simulate keyboard actions (like pressing Enter)
from selenium.webdriver.common.keys import Keys

# ===================== SETUP CHROME OPTIONS =====================

# Create Chrome options object
chrome_options = webdriver.ChromeOptions()

# Keep Chrome browser open after script finishes
chrome_options.add_experimental_option("detach", True)

# ===================== INITIALIZE DRIVER =====================

# Launch Chrome browser with the specified options
driver = webdriver.Chrome(options=chrome_options)

# Maximize the browser window for better visibility
driver.maximize_window()

# Open Wikipedia main page
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# ===================== FIND ELEMENTS =====================

# Locate the total article count link using CSS selector
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

# Click on article count (currently commented out)
# article_count.click()

# Locate "Content portals" link using link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")

# Click on "Content portals" (currently commented out)
# all_portals.click()

# ===================== SEARCH FUNCTIONALITY =====================

# Locate the search input field by its name attribute
search = driver.find_element(By.NAME, value="search")

# Type "Python" into the search box and press Enter
search.send_keys("Python", Keys.ENTER)

# ===================== CLOSE BROWSER =====================

# Close current tab (optional, commented out)
# driver.close()

# Quit the browser session completely (optional, commented out)
# driver.quit()