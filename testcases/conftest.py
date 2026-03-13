import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def browser_setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs",{
            "credentials_enabled_service":False,
            "profile.password_manager_enable":False,
            "profile.password_manager_leak_detection":False
        })
        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "ie":
        driver = webdriver.Ie()
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "headless":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("prefs", {
            "credentials_enabled_service": False,
            "profile.password_manager_enable": False,
            "profile.password_manager_leak_detection": False
        })
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.quit()

def pytest_metadata(metadata):
    metadata["Tester Name"] = "Dhanashri Patil"

def pytest_html_report_title(report):
    report.title = "This is Bank Application Test HTML Report"

