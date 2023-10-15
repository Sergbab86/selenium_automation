from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# credentials
email = 'gosep32179@mugadget.com'
password = 'Qazx1324!'

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
driver.find_element(By.CSS_SELECTOR, 'input#login_password').send_keys(password)
sleep(2)
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
sleep(2)

# Click on captcha and finish log in process
driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])
driver.find_element(By.ID, 'recaptcha-anchor').click()
driver.switch_to.default_content()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'button[name="submit"]').click()
sleep(3)


# Log out
driver.find_element(By.CSS_SELECTOR, 'span#user_avatar_span').click()
sleep(2)
driver.find_element(By.CSS_SELECTOR, 'a[href="/logout/"]').click()
sleep(2)

driver.close()
