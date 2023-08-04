from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Run in headless mode (no browser window)
driver = webdriver.Chrome(executable_path='path/to/chromedriver', options=chrome_options)
purchase_url = 'https://bluestone.com/purchase'  # Replace with the URL of the purchase page
driver.get(purchase_url)
payment_method_radio = driver.find_element(By.ID, 'payment_method')  # Replace with the correct ID of the payment method radio button
payment_method_radio.click()
installment_dropdown = Select(driver.find_element(By.ID, 'installment_option'))  # Replace with the correct ID of the installment dropdown
installment_option = '10+1 Installments'  # Replace with the text of the installment option you want to select
installment_dropdown.select_by_visible_text(installment_option)
# Fill in other required fields (e.g., name, address, etc.)
name_input = driver.find_element(By.ID, 'name')  # Replace with the correct ID of the name input field
name_input.send_keys('shajiya')

address_input = driver.find_element(By.ID, 'address')  # Replace with the correct ID of the address input field
address_input.send_keys('123 Main Street')

# Submit the purchase
purchase_button = driver.find_element(By.ID, 'purchase_button')  # Replace with the correct ID of the purchase button
purchase_button.click()
