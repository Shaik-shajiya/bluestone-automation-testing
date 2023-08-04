from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run in headless mode (no browser window)
driver = webdriver.Chrome(executable_path='path/to/chromedriver', options=chrome_options)
signup_url = 'https://example.com/signup'  # Replace with your signup page URL
driver.get(signup_url)
username_field = driver.find_element(By.NAME, 'username')  # Replace with the correct username input element
email_field = driver.find_element(By.NAME, 'email')  # Replace with the correct email input element
password_field = driver.find_element(By.NAME, 'password')  # Replace with the correct password input element

# Replace 'your_username', 'your_email', and 'your_password' with actual signup credentials
username_field.send_keys('your_username')
email_field.send_keys('your_email@example.com')
password_field.send_keys('your_password')
signup_button = driver.find_element(By.XPATH, '//button[contains(text(), "Sign Up")]')  # Replace with the correct signup button element
signup_button.click()
# Replace '10' with the maximum number of seconds to wait for the signup to complete
wait = WebDriverWait(driver, 10)
wait.until(EC.url_to_be('https://example.com/dashboard'))  # Replace with the URL that indicates successful signup and login
driver.quit()
