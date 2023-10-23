
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Disable notifications in the browser's window and maximize browser's window
option = Options()
option.add_argument('--disable-notifications')
option.add_argument('start-maximized')

# Initialize Chromedriver and open our website
driver = webdriver.Chrome(options=option)
driver.get('https://auto.ria.com/')
wait = WebDriverWait(driver, 20)

# Fill chracteristics for the car

sleep(5)
# Close our webdriver
driver.close()
