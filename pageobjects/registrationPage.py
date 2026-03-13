from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class RegistrationPage:
    username_xpath="//input[@id='username']"
    password_xpath="//input[@id='password']"
    email_xpath="//input[@id='email']"
    phone_xpath="//input[@id='phone']"
    password_rule_text_xpath="//div[@id='passwordRule']"
    create_button_xpath="//button[@id='createUserButton']"
    error_msg_xpath="//div[@id='errorMessage']"
    user_created_successfully_xpath="//div[@id='successMessage']"
    regi_page_heading_xpath="//h2[@id='createUserHeading']"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH,self.username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def set_email(self, email):
        self.driver.find_element(By.XPATH,self.email_xpath).send_keys(email)

    def set_phone(self, phone):
        self.driver.find_element(By.XPATH,self.phone_xpath).send_keys(phone)

    def click_create_button(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element=wait.until(expected_conditions.element_to_be_clickable((By.XPATH,self.create_button_xpath)))
            #element.click()
            self.driver.execute_script("arguments[0].click();", element)
        except Exception as e:
            print(f"Error in click 'create user': {e}")

    def get_usercreated_text(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.user_created_successfully_xpath)))
            text=element.text
            return text
        except Exception as e:
            return self.get_error_msg_text()

    def get_error_msg_text(self):
        try:
            wait = WebDriverWait(self.driver, 15)
            element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.error_msg_xpath)))
            text = element.text
            return text
        except Exception as e:
            return False

    def get_regi_page_heading(self):
        return self.driver.find_element(By.XPATH, self.regi_page_heading_xpath).text
