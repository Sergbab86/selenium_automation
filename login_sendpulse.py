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
email = EMAIL2
password = PASSWORD1

# Disable notifications in the browser's window and maximize browser's window
option = Options()
option.add_argument('--disable-notifications')
option.add_argument('start-maximized')

# Initialize Chromedriver and open our website
driver = webdriver.Chrome(options=option)
driver.get("https://sendpulse.com/")
wait = WebDriverWait(driver, 20)
# Go to log in form
driver.find_element(By.CSS_SELECTOR, 'li.menu-reg__item').click()

# Paste your credentials in the login-form
driver.find_element(By.CSS_SELECTOR, 'input#login_email').send_keys(email)
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'input#login_password').send_keys(password)
sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
sleep(2.5)

# Click on captcha and finish log in process
driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
driver.find_element(By.ID, 'recaptcha-anchor').click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.recaptcha-checkbox-checkmark')))
driver.switch_to.default_content()
sleep(1)
driver.find_element(By.CSS_SELECTOR, 'button[name="submit"]').click()
sleep(1)

# Create a mailing list
driver.find_element(By.CSS_SELECTOR, 'a."btn btn-create"]').click()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[onclick="addAddressBook();"]')))
driver.find_element(By.CSS_SELECTOR, 'button[onclick="addAddressBook();"]').click()

wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.label label-as-link label-yellow arrow_box')))
driver.find_element(By.CSS_SELECTOR, 'span."label label-as-link label-yellow arrow_box"').click()

email_form = driver.find_element(By.CSS_SELECTOR, 'textarea#emailsList')
for email in random_emails:
    email_form.send_keys(email, Keys.ENTER)

driver.find_element(By.CSS_SELECTOR, 'input[value="Upload"],[name="submit_text"]').click()
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#status-description > b:nth-child(1)')))

# Delete created email list
driver.find_element(By.CSS_SELECTOR, 'a.active > span:nth-child(2)').click()
driver.find_element(By.CSS_SELECTOR, 'span."glyphicon glyphicon-option-horizontal"]').click()
driver.find_element(By.XPATH, '(//a[contains(text(),"addressBookDeleteDialog")])').click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '(button:contains("addressBookDelete"))')))
driver.find_element(By.CSS_SELECTOR, '(button:contains("addressBookDelete"))').click()

# Log out
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'img-circle')))
driver.find_element(By.CLASS_NAME, 'img-circle').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'a[href="/logout/"]').click()
sleep(2)
#status-description > b:nth-child(1)
driver.close()
