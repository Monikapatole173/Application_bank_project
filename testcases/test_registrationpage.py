import random

import allure
import pytest
from faker import Faker

from pageobjects.registrationPage import RegistrationPage
from utilities.config_reader import ConfigReader
from utilities.getlogger import GetLogger


@pytest.mark.usefixtures("browser_setup")
class TestRegistrationPage:
    driver = None
    fake=Faker()
    username= fake.user_name()
    #password= fake.password(length=random.randint(6, 12), special_chars=True,upper_case=True,lower_case=True,digits=True)
    password=ConfigReader.get_temp_password()
    email= fake.email()
    phone= fake.phone_number()
    log= GetLogger.get_logger()
    registration_url=ConfigReader.get_registrationurl()

    @allure.title("Bank of America: Banking application user registration page launch varification")
    @allure.epic("Online Banking Application: Registration Process")
    @allure.story("As a user, I want to launch user registration page of the application")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.smoke
    # @pytest.mark.skip
    @pytest.mark.dependency(name="test_homepage_launch_003")
    def test_registration_page_launch_009(self):
        regi_page = RegistrationPage(self.driver)
        self.log.info(f"launching registration page url: {self.registration_url}....")
        self.driver.get(self.registration_url)
        self.driver.implicitly_wait(3)
        if regi_page.get_regi_page_heading() == ConfigReader.get_regi_page_heading():
            self.log.info(f"Landed on registration page successfully and taking screenshots....")
            self.driver.save_screenshot(".\\Screenshots\\registrationPage\\registration_page_landed_successfully.png")
            allure.attach.file(".\\Screenshots\\registrationPage\\registration_page_landed_successfully.png",attachment_type=allure.attachment_type.PNG)
        else:
            self.log.info(f"Application registration page launch failed and taking screenshot.....")
            self.driver.save_screenshot(".\\Screenshots\\registrationPage\\application_registration_page_launch_failed.png")
            allure.attach.file(".\\Screenshots\\registrationPage\\application_registration_page_launch_failed.png",attachment_type=allure.attachment_type.PNG)
        assert self.driver.title == ConfigReader.get_regi_page_heading(), "Application registration page launch failed"

    @allure.title("Bank of America: Banking application user registration process varification")
    @allure.epic("Online Banking Application: Registration Process")
    @allure.story("As a user, I want to register to the application")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.suite("Bank of America Automation Test Project")
    @pytest.mark.regression
    # @pytest.mark.skip
    @pytest.mark.flaky(reruns=1,reruns_delay=3)
    @pytest.mark.dependency(name="test_registration_page_launch_009")
    def test_user_registration_010(self):
        regi_page = RegistrationPage(self.driver)
        self.log.info(f"launching registration page url: {self.registration_url}....")
        self.driver.get(self.registration_url)
        self.driver.implicitly_wait(3)
        self.log.info(f"Setting user name....................")
        regi_page.set_username(self.username)
        self.log.info(f"Setting password as : {self.password}....................")
        regi_page.set_password(self.password)
        self.log.info(f"Setting email....................")
        regi_page.set_email(self.email)
        self.log.info(f"Setting phone number....................")
        regi_page.set_phone(self.phone)
        self.log.info(f"Clicking on Create user button....................")
        regi_page.click_create_button()
        self.driver.implicitly_wait(3)
        self.log.info(f"Create user button clicked successfully....................")
        text = regi_page.get_usercreated_text()
        self.driver.implicitly_wait(2)
        self.log.info(f"getting user created text: {text}....................")
        if text =="User created successfully":
            testcase_status="Pass"
            self.log.info(f"User: {self.username} created successfully and taking screenshots....................")
            self.driver.save_screenshot(f".\\Screenshots\\registrationPage\\user_{self.username}_created_successfully.png")
            allure.attach.file(f".\\Screenshots\\registrationPage\\user_{self.username}_created_successfully.png",attachment_type=allure.attachment_type.PNG)
        elif text =="Username already exists":
            testcase_status = "Pass"
            self.log.info(f"User: {self.username} already exists and taking screenshots....................")
            self.driver.save_screenshot(f".\\Screenshots\\registrationPage\\user:_{self.username}_already_exists.png")
            allure.attach.file(f".\\Screenshots\\registrationPage\\user:_{self.username}_already_exists.png",attachment_type=allure.attachment_type.PNG)
        elif text == "Phone number already exists":
            testcase_status = "Pass"
            self.log.info(f"Phone: {self.phone} already exists and taking screenshots....................")
            self.driver.save_screenshot(f".\\Screenshots\\registrationPage\\phone:_{self.phone}_already_exists.png")
            allure.attach.file(f".\\Screenshots\\registrationPage\\phone:_{self.phone}_already_exists.png",attachment_type=allure.attachment_type.PNG)
        elif text == "Email already exists":
            testcase_status = "Pass"
            self.log.info(f"Email: {self.email} already exists and taking screenshots....................")
            self.driver.save_screenshot(f".\\Screenshots\\registrationPage\\email:_{self.email}_already_exists.png")
            allure.attach.file(f".\\Screenshots\\registrationPage\\email:_{self.email}_already_exists.png",attachment_type=allure.attachment_type.PNG)
        else:
            testcase_status="Fail"
            self.driver.save_screenshot(f".\\Screenshots\\registrationPage\\application_registration_failed.png")
            allure.attach.file(".\\Screenshots\\registrationPage\\application_registration_failed.png",attachment_type=allure.attachment_type.PNG)
        assert testcase_status=="Pass", "User creation failed"