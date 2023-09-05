import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.fixture()
def setUp():
    print("\nRunning method level setUp\n")
    yield
    print("\nRunning method level tearDown\n")

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("\nRunning one time setUp\n")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
