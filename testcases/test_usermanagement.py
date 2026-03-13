import allure
import pytest

from pageobjects.loginpage import LoginPage
from pageobjects.usermanagement import UserManagement
from utilities.config_reader import ConfigReader
from utilities.getlogger import GetLogger


@pytest.mark.usefixtures("browser_setup")
class Test_User_Management:

    driver = None
    log = GetLogger.get_logger()
    search_username = ConfigReader.get_search_username()
    username=ConfigReader.get_username()
    password=ConfigReader.get_password()
    login_url= ConfigReader.get_loginurl()

    @allure.title("Bank of America: Banking application user management page launch varification")
    @allure.epic("Online Banking Application: User Management Process")
    @allure.story("As a user, I want to launch user management page of the application")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.smoke
    # @pytest.mark.skip
    @pytest.mark.dependency(name="test_user_login_002")
    def test_landing_user_management_011(self):
        self.log.info("Launching user login page url...............")
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(5)
        login_page = LoginPage(self.driver)
        user_mgnt=UserManagement(self.driver)
        self.log.info("Setting username field.....")
        login_page.set_username(self.username)
        self.log.info("Setting password field.....")
        login_page.set_password(self.password)
        self.log.info("Clicking login button.....")
        login_page.click_login_button()
        if login_page.check_visibility_of_logged_in_user(self.username):
            self.log.info(f"User : {self.username} logged in Successfully and taking screenshot..... ")
            self.driver.save_screenshot(f".\\Screenshots\\user_management\\user_{self.username}_loggedin_Successfully.png")
            allure.attach.file(f".\\Screenshots\\user_management\\user_{self.username}_loggedin_Successfully.png",attachment_type=allure.attachment_type.PNG)
            self.log.info("Clicking on User Management button.......")
            user_mgnt.click_user_management_button()
            self.driver.implicitly_wait(3)
            if user_mgnt.get_user_mgnt_heading() == ConfigReader.get_user_management_heading():
                self.log.info("Landed on User Management page successfully and taking screenshot.......")
                self.driver.save_screenshot(f".\\Screenshots\\user_management\\landed_on_user_mgnt_Successfully.png")
                allure.attach.file(f".\\Screenshots\\user_management\\landed_on_user_mgnt_Successfully.png",attachment_type=allure.attachment_type.PNG)
                testcase_status="Pass"
                self.log.info("Clicking on logout button.......")
                user_mgnt.click_logout_button()
                self.log.info("Logged out successfully.......")
            else:
                self.log.info("Landing on User Management page Failed and taking screenshot.......")
                self.driver.save_screenshot(f".\\Screenshots\\user_management\\landing_on_user_mgnt_Failed.png")
                allure.attach.file(f".\\Screenshots\\user_management\\landing_on_user_mgnt_Failed.png",attachment_type=allure.attachment_type.PNG)
                testcase_status="Fail"

            assert testcase_status == "Pass","Landing on User Management Page is Failed"

    @allure.title("Bank of America: Banking application user management- Search user varification")
    @allure.epic("Online Banking Application: User Management Process")
    @allure.story("As a user, I want to land on user management page and search the specific user")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.regression
    @pytest.mark.dependency(name="test_landing_user_management_011")
    def test_user_management_search_user_012(self):
        self.log.info("Launching user login page url...............")
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(5)
        login_page = LoginPage(self.driver)
        user_mgnt=UserManagement(self.driver)
        self.log.info("Setting username field.....")
        login_page.set_username(self.username)
        self.log.info("Setting password field.....")
        login_page.set_password(self.password)
        self.log.info("Clicking login button.....")
        login_page.click_login_button()
        if login_page.check_visibility_of_logged_in_user(self.username):
            self.log.info(f"User : {self.username} logged in Successfully and taking screenshot..... ")
            self.driver.save_screenshot(f".\\Screenshots\\user_management\\user_{self.username}_loggedin_Successfully.png")
            allure.attach.file(f".\\Screenshots\\user_management\\user_{self.username}_loggedin_Successfully.png",attachment_type=allure.attachment_type.PNG)
            self.log.info("Clicking on User Management button.......")
            user_mgnt.click_user_management_button()
            self.driver.implicitly_wait(3)
            self.log.info("Landed on User Management page successfully.......")
            self.log.info("Sending search user name for searching.......")
            user_mgnt.set_search_username_field(self.search_username)
            self.driver.implicitly_wait(2)
            user_mgnt.click_search_user_button()
            if user_mgnt.get_edit_user_page_heading() == ConfigReader.get_edit_user_page_heading():
                testcase_status="Pass"
                self.log.info(f"User : {self.search_username} search is Successfully and taking screenshot..... ")
                self.driver.save_screenshot(f".\\Screenshots\\user_management\\user_{self.search_username}_searched_Successfully.png")
                allure.attach.file(f".\\Screenshots\\user_management\\user_{self.search_username}_searched_Successfully.png",attachment_type=allure.attachment_type.PNG)
                self.log.info("Clicking on logout button.......")
                user_mgnt.click_logout_button()
                self.log.info("Logged out successfully.......")
            elif user_mgnt.get_user_not_found_error() == "User not found":
                testcase_status = "Pass"    # test is Passed. Because it shows proper error, if user not exists
                self.log.info("Error displayed: User not found and taking screenshot.......")
                self.driver.save_screenshot(f".\\Screenshots\\user_management\\error_user_not_found.png")
                allure.attach.file(f".\\Screenshots\\user_management\\error_user_not_found.png",attachment_type=allure.attachment_type.PNG)

            else:
                testcase_status = "Fail"
                self.log.info("User search Failed & taking screenshot.......")
                self.driver.save_screenshot(f".\\Screenshots\\user_management\\error_user_search_failed.png")
                allure.attach.file(f".\\Screenshots\\user_management\\error_user_search_failed.png",attachment_type=allure.attachment_type.PNG)

            assert testcase_status == "Pass", "User search is Failed"



