from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Initialize the Chrome driver
driver = webdriver.Chrome()

try:
    # Open the Rutracker login page
    driver.get("https://rutracker.org/forum/index.php")

    # Locate and fill the login form
    username_field = driver.find_element(By.NAME, "login_username")
    password_field = driver.find_element(By.NAME, "login_password")
    login_button = driver.find_element(By.NAME, "login")

    username_field.send_keys("Сергей Бабяк")
    password_field.send_keys("BFUXa")
    login_button.click()

    # Wait until the login process is complete
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "logged-in-username")))

    # Navigate to "Еженедельные обновления Либрусека"
    driver.get("https://rutracker.org/forum/viewforum.php?f=XXX")  # Replace XXX with the appropriate forum ID

    # Search for "Manacled" in "СПИСОК КНИГ"
    search_box = driver.find_element(By.NAME, "nm")
    search_box.send_keys("Manacled")
    search_box.send_keys(Keys.RETURN)

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "tTitle")))

    # Parse and print the search results
    results = driver.find_elements(By.CSS_SELECTOR, "tr[id='trs-tr-6607814'] div[class='wbr t-title']")
    for result in results:
        print(result.text)
        print(result.get_attribute("href"))

finally:
    # Close the browser
    time.sleep(5)
    driver.quit()
