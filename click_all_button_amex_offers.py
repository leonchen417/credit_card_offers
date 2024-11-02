from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setup Chrome options to connect to the existing instance
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"  # Ensure this matches the port from the debugging command

# Attach Selenium to the existing Chrome session
driver = webdriver.Chrome(options=options)

# Example: Navigate to the desired page
driver.get("https://global.americanexpress.com/offers/eligible")  # Replace with the website you want to interact with

time.sleep(30)

# Find and click all "Add to Cart" buttons
add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[.//span[text()='Add to Card']]")
# import pdb; pdb.set_trace()

for button in add_to_cart_buttons:
    try:
        ActionChains(driver).move_to_element(button).click(button).perform()
        time.sleep(2)  # Adjust if necessary for any loading times
    except Exception as e:
        print(f"Error clicking button: {e}")

# Optional: Leave the browser open, or close it with driver.quit()

