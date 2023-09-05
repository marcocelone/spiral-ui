from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class DucksPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home_page_title = "Ducks - Google Search"
    _navigation_menu = "//div[@role='navigation']"
    _ducks_section = "[jscontroller='M0hWhd']"
    _people_ask_section = "[data-initq='ducks']"
    _wikipedia = "//h3[text()='Duck - Wikipedia']"


    def verify_ducks_section(self):
        result = self.isElementPresent(self._ducks_section, locatorType='css')
        return result

    def verify_people_ask_section(self):
        result = self.isElementPresent(self._people_ask_section, locatorType='css')
        return result

    def verify_navigation_menu(self):
        result = self.isElementPresent(self._navigation_menu, locatorType='xpath')
        return result

    def verify_wikipedia(self):
        result = self.isElementPresent(self._wikipedia, locatorType='xpath')
        return result


