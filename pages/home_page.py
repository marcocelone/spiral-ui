from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class HomePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _text_area = 'APjFqb'

    def text_search(self, text):
        self.waitForElement(self._text_area, locatorType='id')
        self.sendKeys(text, self._text_area, locatorType='id')

    def verify_search_successfull(self, page_title):
        result = self.get_title(page_title)
        return result
