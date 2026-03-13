import time

import allure
import pytest

from pageobjects.homepage import HomePage
from pageobjects.loginpage import LoginPage
from utilities.config_reader import ConfigReader
from utilities.getlogger import GetLogger


@pytest.mark.usefixtures("browser_setup")
class TestHomepage:
    driver = None
    log = GetLogger.get_logger()
    home_url = ConfigReader.get_homeurl()
    home_title= ConfigReader.get_hometitle()
    signup_heading=ConfigReader.get_signupheading()

    @allure.title("Bank of America: Banking application home page launch varification")
    @allure.epic("Online Banking Application")
    @allure.story("As a user, I want to launch homepage")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.smoke
    def test_homepage_launch_003(self):
        self.log.info(f"launch home page url: {self.home_url}.....")
        self.driver.get(self.home_url)
        self.log.info(f"landed on home page url and checking title.....")
        if self.driver.title==self.home_title:
            self.log.info(f"Home page title is equal to {self.home_title} & taking screenshots...")
            self.driver.save_screenshot(".\\Screenshots\\homePage\\home_page_title_success.png")
            allure.attach.file(".\\Screenshots\\homePage\\home_page_title_success.png",attachment_type=allure.attachment_type.PNG)
        else:
            self.log.info(f"Home page title is not equal to {self.home_title} & taking screenshots...")
            self.driver.save_screenshot(".\\Screenshots\\homePage\\home_page_title_fail.png")
            allure.attach.file(".\\Screenshots\\homePage\\home_page_title_fail.png",attachment_type=allure.attachment_type.PNG)

    @allure.title("Bank of America: Banking application homepage to loging page navigation varification")
    @allure.epic("Online Banking Application")
    @allure.story("As a user, I want to navigate from homepage to login page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.dependency(name="test_homepage_launch_003")
    @pytest.mark.smoke
    def test_homepage_to_loginpage_navigation_004(self):
        self.log.info(f"launch home page url: {self.home_url}.....")
        self.driver.get(self.home_url)
        self.driver.implicitly_wait(5)
        homepage= HomePage(self.driver)
        self.log.info("Landed on home page and clicking on login...")
        homepage.click_on_login()
        self.driver.implicitly_wait(5)
        self.log.info("Landed on Login page...")
        loginpage = LoginPage(self.driver)
        login_heading = loginpage.get_loginpage_heading()
        self.log.info("Verifying login page heading...")
        if self.driver.title==login_heading:
            testcase_status = "Pass"
            self.log.info("login page heading verified & taking screenshots...")
            self.driver.save_screenshot(".\\Screenshots\\homePage\\login_page_title_success.png")
            allure.attach.file(".\\Screenshots\\homePage\\login_page_title_success.png",attachment_type=allure.attachment_type.PNG)
        else:
            testcase_status = "Fail"
            self.log.info("login page heading not verified & taking screenshots...")
            self.driver.save_screenshot(".\\Screenshots\\homePage\\login_page_title_fail.png")
            allure.attach.file(".\\Screenshots\\homePage\\login_page_title_fail.png",attachment_type=allure.attachment_type.PNG)
        assert  testcase_status=="Pass", "Navigation Failed"


    @allure.title("Bank of America: Banking application home page to login and back to home page navigation varification")
    @allure.epic("Online Banking Application")
    @allure.story("As a user, I want to navigate back and forth from homepage to login page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.dependency(name="test_homepage_launch_003")
    @pytest.mark.smoke
    def test_homepage_login_home_navigation_005(self):
        self.log.info(f"launch home page url: {self.home_url}.....")
        self.driver.get(self.home_url)
        self.driver.implicitly_wait(5)
        self.log.info("Landed on home page and clicking on login page...")
        homepage = HomePage(self.driver)
        self.log.info("Landed on Login page...")
        homepage.click_on_login()
        self.driver.implicitly_wait(3)
        loginpage = LoginPage(self.driver)
        login_heading = loginpage.get_loginpage_heading()
        self.log.info("Verifying login page heading...")
        self.driver.implicitly_wait(2)
        if self.driver.title == login_heading:
            self.log.info("login page heading verified & taking screenshots...")
            self.driver.save_screenshot(".\\Screenshots\\homePage\\login_page_title_success.png")
            allure.attach.file(".\\Screenshots\\homePage\\login_page_title_success.png",attachment_type=allure.attachment_type.PNG)
            self.driver.back()
            self.driver.implicitly_wait(1)
            if self.driver.title == self.home_title:
                testcase_status = "Pass"
                self.log.info(f"Home page title is verified & taking screenshots...")
                self.driver.save_screenshot(".\\Screenshots\\homePage\\backtohome_page_title_success.png")
                allure.attach.file(".\\Screenshots\\homePage\\backtohome_page_title_success.png",attachment_type=allure.attachment_type.PNG)
            else:
                testcase_status = "Fail"
                self.log.info(f"Page title is not equal to {self.home_title} & taking screenshots...")
                self.driver.save_screenshot(".\\Screenshots\\homePage\\backtohome_page_title_fail.png")
                allure.attach.file(".\\Screenshots\\homePage\\backtohome_page_title_fail.png",attachment_type=allure.attachment_type.PNG)

        else:
            testcase_status = "Fail"
            self.log.info("login page heading not verified & taking screenshots...")
            self.driver.save_screenshot(".\\Screenshots\\homePage\\login_page_title_fail.png")
            allure.attach.file(".\\Screenshots\\homePage\\login_page_title_fail.png",attachment_type=allure.attachment_type.PNG)
        assert testcase_status == "Pass", "Navigation Failed"


    @allure.title("Bank of America: Banking application home page to signup page navigation varification")
    @allure.epic("Online Banking Application")
    @allure.story("As a user, I want to navigate from homepage to signup page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.dependency(name="test_homepage_launch_003")
    @pytest.mark.smoke
    def test_homepage_to_signup_navigation_006(self):
        self.log.info(f"launch home page url: {self.home_url}.....")
        self.driver.get(self.home_url)
        self.driver.implicitly_wait(5)
        self.log.info("landed on home page and clicking on signup...")
        homepage= HomePage(self.driver)
        self.log.info("Landed on signup page & verifying title...")
        homepage.click_on_signup()
        self.driver.implicitly_wait(5)
        #signuppage = SignupPage(self.driver)
        #signup_heading = signuppage.get_signuppage_heading()
        self.log.info("Verifying Signup page heading...")
        if self.driver.title==self.signup_heading:
            testcase_status = "Pass"
            self.log.info("Signup page heading verified & taking screenshots...")
            self.driver.save_screenshot(".\\Screenshots\\homePage\\signup_page_title_success.png")
            allure.attach.file(".\\Screenshots\\homePage\\signup_page_title_success.png",attachment_type=allure.attachment_type.PNG)
        else:
            testcase_status = "Fail"
            self.log.info("login page heading not verified & taking screenshots...")
            self.driver.save_screenshot(".\\Screenshots\\homePage\\signup_page_title_fail.png")
            allure.attach.file(".\\Screenshots\\homePage\\signup_page_title_fail.png",attachment_type=allure.attachment_type.PNG)
        assert testcase_status=="Pass", "Navigation Failed"

    @allure.title("Bank of America: Banking application home page to signup and back to homepage navigation varification")
    @allure.epic("Online Banking Application")
    @allure.story("As a user, I want to navigate back and forth from homepage to signup page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.dependency(name="test_homepage_launch_003")
    @pytest.mark.smoke
    def test_homepage_signup_home_navigation_007(self):
        self.log.info(f"launch home page url: {self.home_url}.....")
        self.driver.get(self.home_url)
        self.driver.implicitly_wait(5)
        self.log.info("Landed on home page and clicking on signup page...")
        homepage = HomePage(self.driver)
        homepage.click_on_signup()
        self.log.info("Landed on signup page...")
        self.driver.implicitly_wait(5)
        # signuppage = SignupPage(self.driver)
        # signup_heading = signuppage.get_signuppage_heading()
        self.log.info("Verifying signup page heading...")
        if self.driver.title == self.signup_heading:
            self.log.info("signup page heading verified & taking screenshots...")
            self.driver.save_screenshot(".\\Screenshots\\homePage\\signup_page_title_success.png")
            allure.attach.file(".\\Screenshots\\homePage\\signup_page_title_success.png",attachment_type=allure.attachment_type.PNG)
            self.driver.back()
            if self.driver.title == self.home_title:
                testcase_status="Pass"
                self.log.info(f"Home page title is verified & taking screenshots...")
                self.driver.save_screenshot(".\\Screenshots\\homePage\\backtohome_frm_signupPage_title_success.png")
                allure.attach.file(".\\Screenshots\\homePage\\backtohome_frm_signupPage_title_success.png",attachment_type=allure.attachment_type.PNG)
            else:
                testcase_status = "Fail"
                self.log.info(f"Home page title is not equal to {self.home_title} & taking screenshots...")
                self.driver.save_screenshot(".\\Screenshots\\homePage\\backtohome_frm_signupPage_title_fail.png")
                allure.attach.file(".\\Screenshots\\homePage\\acktohome_frm_signupPage_title_fail.png",attachment_type=allure.attachment_type.PNG)
        else:
            testcase_status = "Fail"
            self.log.info("Signup page heading not verified & taking screenshots...")
            self.driver.save_screenshot(".\\Screenshots\\homePage\\signup_page_title_fail.png")
            allure.attach.file(".\\Screenshots\\homePage\\signup_page_title_fail.png",attachment_type=allure.attachment_type.PNG)

        assert testcase_status == "Pass", "Navigation Failed"




