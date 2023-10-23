
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

# Fill characteristics for the car
driver.find_element(By.CSS_SELECTOR, '#brandTooltipBrandAutocomplete-brand').click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="item"][contains(text(),"Toyota")]')))
driver.find_element(By.XPATH, '//a[@class="item"][contains(text(),"Toyota")]').click()
driver.find_element(By.CSS_SELECTOR, 'label[data-text="Модель"]').click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="item"][contains(text(), "Sequoia")]')))
driver.find_element(By.XPATH, '//a[@class="item"][contains(text(), "Sequoia")]').click()
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# Sort the result by date(desc)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#sortCheckedElement')))
driver.find_element(By.CSS_SELECTOR, 'a#sortCheckedElement').click()
driver.find_element(By.CSS_SELECTOR, 'a[data-value="dates.created.desc"]').click()

# Remove custom
# driver.find_element(By.CSS_SELECTOR, 'span[data-name="custom.not"],a[title="удалить"]').click()

sleep(10)
# Close our webdriver
driver.close()
