import allure
import pytest

from pageobjects.loginpage import LoginPage
from utilities.config_reader import ConfigReader
from utilities.getlogger import GetLogger
from utilities.read_xlsUtility import XlsUtility


@pytest.mark.usefixtures("browser_setup")
class TestLoginPage:
    driver = None
    log = GetLogger.get_logger()
    login_url= ConfigReader.get_loginurl()
    username=ConfigReader.get_username()
    password=ConfigReader.get_password()

    @allure.title("Bank of America: Banking application launching login page varification")
    @allure.epic("Online Banking Application: Login Process")
    @allure.story("As a user, I want to launch login page")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.smoke
    @pytest.mark.dependency(name="test_homepage_launch_003")
    def test_login_page_001(self):
        self.log.info(f"Launching application login page with url: '{self.login_url}'.....")
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(5)
        self.log.info("Checking page title.....")
        if self.driver.title == "Login":
            self.log.info(f"Application login page launched successfully and taking screenshot.....")
            self.driver.save_screenshot(".\\Screenshots\\loginPage\\application_login_page_launched_successfully.png")
            allure.attach.file(".\\Screenshots\\loginPage\\application_login_page_launched_successfully.png",attachment_type=allure.attachment_type.PNG)
        else:
            self.log.info(f"Application login page launch failed and taking screenshot.....")
            self.driver.save_screenshot(".\\Screenshots\\loginPage\\application_login_page_launch_failed.png")
            allure.attach.file(".\\Screenshots\\loginPage\\application_login_page_launch_failed.png",attachment_type=allure.attachment_type.PNG)
        assert self.driver.title == "Login"

    @allure.title("Bank of America: Banking application user login process varification")
    @allure.epic("Online Banking Application: Login Process")
    @allure.story("As a user, I want to login with valid credentials to the application")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.regression
    #@pytest.mark.skip
    @pytest.mark.dependency(name="test_login_page_001")
    def test_user_login_002(self):
        self.log.info(f"Launching application login page with username: '{self.login_url}'.....")
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(5)
        login_page = LoginPage(self.driver)
        self.log.info("Setting username field.....")
        login_page.set_username(self.username)
        self.log.info("Setting password field.....")
        login_page.set_password(self.password)
        self.log.info("Clicking login button.....")
        login_page.click_login_button()
        if login_page.check_visibility_of_logged_in_user(self.username):
            actual_result = "login_pass"
            self.log.info(f"User : {self.username} logged in Successfully and taking screenshot..... ")
            self.driver.save_screenshot(f".\\Screenshots\\loginPage\\user_{self.username}_loggedin_Successfully.png")
            allure.attach.file(f".\\Screenshots\\loginPage\\user_{self.username}_loggedin_Successfully.png",attachment_type=allure.attachment_type.PNG)
            self.log.info("Logging out.......")
            login_page.click_logout_button()
            self.log.info("Logged-out Successfully........")
        else:
            actual_result = "login_fail"
            self.log.info(f"User : {self.username} logged in Failed and taking screenshot..... ")
            self.driver.save_screenshot(f".\\Screenshots\\loginPage\\user_{self.username}_login_Failed.png")
            allure.attach.file(f".\\Screenshots\\loginPage\\user_{self.username}_login_Failed",attachment_type=allure.attachment_type.PNG)

    @allure.title("Bank of America: Banking application user login process varification with valid and invalid credentials")
    @allure.epic("Online Banking Application: Login Process")
    @allure.story("As a user, I want to login to the application using DDT")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.suite("Bank of America Automation Test Project")
    # @pytest.mark.skip
    @pytest.mark.dependency(name="test_login_page_001")
    def test_user_login_with_DDT_008(self):
        excel_file = ConfigReader.get_excel_file_name()
        sheetname= ConfigReader.get_excel_sheet_name()
        max_rows=XlsUtility.get_max_rows(excel_file,sheetname)
        for i in range(2,max_rows+1):
            username=XlsUtility.read_excel_file(excel_file,sheetname,i,2)
            password = XlsUtility.read_excel_file(excel_file, sheetname, i, 3)
            self.log.info(f"Launching application login page: '{self.login_url}'.....")
            self.driver.get(self.login_url)
            self.driver.implicitly_wait(5)
            login_page = LoginPage(self.driver)
            self.log.info("Setting username field.....")
            login_page.set_username(username)
            self.log.info("Setting password field.....")
            login_page.set_password(password)
            self.log.info("Clicking login button.....")
            login_page.click_login_button()
            if login_page.check_visibility_of_logged_in_user(username):
                actual_result = "login_pass"
                XlsUtility.write_excel_file(excel_file, sheetname, i, 5, actual_result)
                self.log.info(f"User : {username} logged in Successfully and taking screenshot..... ")
                self.driver.save_screenshot(f".\\Screenshots\\loginPage\\user_{username}_loggedin_Successfully.png")
                allure.attach.file(f".\\Screenshots\\loginPage\\user_{username}_loggedin_Successfully.png",attachment_type=allure.attachment_type.PNG)
                self.log.info("Logging out.......")
                login_page.click_logout_button()
                self.log.info("Logged-out Successfully........")
            else:
                actual_result = "login_fail"
                XlsUtility.write_excel_file(excel_file, sheetname, i, 5, actual_result)
                self.log.info(f"User : {username} logged in Failed and taking screenshot..... ")
                self.driver.save_screenshot(f".\\Screenshots\\loginPage\\user_{username}_login_Failed.png")
                allure.attach.file(f".\\Screenshots\\loginPage\\user_{username}_login_Failed.png",attachment_type=allure.attachment_type.PNG)

            if actual_result == XlsUtility.read_excel_file(excel_file,sheetname,i,4):
                testcase_status="Pass"
            else:
                testcase_status = "Fail"
            XlsUtility.write_excel_file(excel_file, sheetname, i, 6, testcase_status)
            assert testcase_status=="Pass", "User Login Failed"








