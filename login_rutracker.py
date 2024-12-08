import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from email_generator import random_emails
from emails_passwords import *

# credentials
email = "Сергей Бабяк"
password = "BFUXa"

# Disable notifications in the browser's window and maximize browser's window
option = Options()
option.add_argument('--disable-notifications')
option.add_argument('start-maximized')

# Initialize Chromedriver and open our website
driver = webdriver.Chrome(options=option)
driver.get("https://rutracker.org/forum/index.php")
wait = WebDriverWait(driver, 10)
# Go to log in form
driver.find_element(By.XPATH, "//b[contains(text(),'Вход')]").click()
# Paste your credentials in the login-form
driver.find_element(By.CSS_SELECTOR, '#top-login-uname').send_keys(email)
sleep(1)
driver.find_element(By.CSS_SELECTOR, '#top-login-pwd').send_keys(password)
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#top-login-btn").click()
sleep(2.5)
# Wait for the Tracker to load
wait.until(EC.element_to_be_clickable((By.XPATH, "//b[contains(text(),'Трекер')]")))
# Go to tracker
driver.find_element(By.XPATH, "//b[contains(text(),'Трекер')]").click()
# Find and click Librusek button
driver.find_element(By.CSS_SELECTOR, '#title-search').send_keys("Еженедельные обновления Либрусека")
driver.find_element(By.CSS_SELECTOR, "#tr-submit-btn").click()

# Parse and print the search results
results = driver.find_elements(By.CSS_SELECTOR, "tr[id='trs-tr-6607814'] div[class='wbr t-title']")
for result in results:
    print(result.text)
    print(result.get_attribute("href"))

time.sleep(5)
driver.close()
