"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class
        """
        self.browser = browser
    """
        Set chrome driver environment based on OS

        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration
        Returns:
            'WebDriver Instance'
        """
        base_url = "https://www.google.com/"
        if self.browser == "chrome":
            # Set ie driver
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome-headless":
            options = Options()
            options.add_argument("--headless=new")
            # Set chrome headless driver
            driver = webdriver.Chrome(options=options)
        else:
            driver = webdriver.Chrome()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(base_url)
        return driver
