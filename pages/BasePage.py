
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://auto.ria.com/"

    def open(self, url):
        self.driver.get(self.base_url + url)

    def find_element(self, by, value, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return element
        except:
            raise Exception(f"Element not found: {by} = {value}")

    def click_element(self, by, value, timeout=10):
        element = self.find_element(by, value, timeout)
        element.click()

    def type_text(self, by, value, text, timeout=10):
        element = self.find_element(by, value, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value, timeout=10):
        element = self.find_element(by, value, timeout)
        return element.text

    def wait_for_element_to_be_visible(self, by, value, timeout=10):
        element = self.find_element(by, value, timeout)
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of(element)
        )
