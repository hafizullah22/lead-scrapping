from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
chrome_options.add_argument("--lang=en")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Open Google Maps search page
driver.get('https://www.google.com/maps/search/laptop+shop+near+mirpur')
time.sleep(5)

# Loop through result items (adjust range as needed)
for i in range(3, 12, 2):
    j = str(i)
    try:
        # Click on each result item
        result_xpath = f'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[{j}]/div/a'
        info = driver.find_element(By.XPATH, result_xpath)
        info.click()
        time.sleep(10)

        # Extract name
        try:
            name = driver.find_element(By.XPATH, '//h1[contains(@class,"DUwDvf")]').text
            print("Name:", name)
        except:
            print("Name not found")

        # Extract address
        try:
            address = driver.find_element(By.XPATH, '//button[@data-item-id="address"]/div/div[2]/div').text
            print("Address:", address)
        except:
            print("Address not found")

        # Extract phone number
        try:
            phone = driver.find_element(By.XPATH, '//button[@data-item-id="phone"]/div/div[2]/div').text
            print("Phone:", phone)
        except:
            print("Phone not found")

        print('-' * 40)
        time.sleep(5)

    except Exception as e:
        print(f"Error processing item {i}: {e}")
        continue

# Finish
driver.quit()

