
from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """
    A class for main page locators.
    All main page locators should come here
    """
    BRAND_SEARCH_BUTTON =(By.CSS_SELECTOR, '#brandTooltipBrandAutocomplete-brand')
    BRAND_SCROLLBAR = (By.XPATH, '//a[@class="item"][contains(text(),"Toyota")]')
    MODEL_SEARCH_BUTTON = (By.CSS_SELECTOR, 'label[data-text="Модель"]')
    MODEL_SCROLLBAR = (By.XPATH, '//a[@class="item"][contains(text(), "Sequoia")]')
    SUBMIT = (By.CSS_SELECTOR, 'button[type="submit"]')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should
     come here"""
    SELECT_SORT = (By.CSS_SELECTOR, 'a#sortCheckedElement')
    DATE_SORT = (By.CSS_SELECTOR, 'a[data-value="dates.created.desc"]')

