from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run in headless mode (no browser window)
driver = webdriver.Chrome(executable_path='path/to/chromedriver', options=chrome_options)
page_url = 'https://bluestone.com'  # Replace with the URL of the web page you want to test
driver.get(page_url)
expected_text = "Welcome to Example.com"  # Replace with the text you expect to find on the page
element_locator = (By.XPATH, "//*[contains(text(), 'Welcome to Example.com')]")  # Replace with the correct locator for the element containing the text

# Find the element using the specified locator
element = driver.find_element(*element_locator)

# Get the actual text from the element
actual_text = element.text

# Compare the actual text with the expected text
if expected_text in actual_text:
    print("Text verification passed!")
else:
    print(f"Text verification failed. Expected: '{expected_text}', Actual: '{actual_text}'")
driver.quit()
