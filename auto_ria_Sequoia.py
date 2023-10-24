
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators.search_locators import MainPageLocators, SearchResultsPageLocators

# Disable notifications in the browser's window and maximize browser's window
option = Options()
option.add_argument('--disable-notifications')
option.add_argument('start-maximized')

# Initialize Chromedriver and open our website
driver = webdriver.Chrome(options=option)
driver.get('https://auto.ria.com/')
wait = WebDriverWait(driver, 20)
actions = ActionChains(driver)

driver.implicitly_wait(10)


# Fill characteristics for the car
driver.find_element(*MainPageLocators.BRAND_SEARCH_BUTTON).click()
wait.until(EC.element_to_be_clickable(MainPageLocators.BRAND_SCROLLBAR))
driver.find_element(*MainPageLocators.BRAND_SCROLLBAR).click()
driver.find_element(*MainPageLocators.MODEL_SEARCH_BUTTON).click()
wait.until(EC.element_to_be_clickable(MainPageLocators.MODEL_SCROLLBAR))
driver.find_element(*MainPageLocators.MODEL_SCROLLBAR).click()
driver.find_element(*MainPageLocators.SUBMIT).click()

# Sort the result by date(desc)
wait.until(EC.element_to_be_clickable(SearchResultsPageLocators.SELECT_SORT))
driver.find_element(*SearchResultsPageLocators.SELECT_SORT).click()
driver.find_element(*SearchResultsPageLocators.DATE_SORT).click()

# Close our webdriver
driver.close()
