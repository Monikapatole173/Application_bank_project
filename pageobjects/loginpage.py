import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    username_field_xpath = "//input[@id='username']"
    password_field_xpath = "//input[@id='password']"
    login_button_xpath = "//button[@id='loginButton']"
    logged_in_user_xpath= "//div[@class='username']"
    logout_option_xpath ="//a[normalize-space()='Logout']"
    login_page_heading= "//h2[@id='loginHeading']"


    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.username_field_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password)

    def click_login_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH,self.login_button_xpath)))
        submit=self.driver.find_element(By.XPATH,self.login_button_xpath)
        self.driver.execute_script('arguments[0].click()', submit)

    def check_visibility_of_logged_in_user(self, username):
        try:
            wait = WebDriverWait(self.driver, 10)
            element=wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.logged_in_user_xpath)))
            text=element.text
            time.sleep(2)
            #print(f"Text user is={text} and 'Logged in as: {username}'")
            if text == f"Logged in as: {username}":
              return True
        except Exception as e:
            return False

    def click_logout_button(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            element=wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.logout_option_xpath)))
            #element.click()
            self.driver.execute_script('arguments[0].click()', element)
        except Exception as e:
            print("Error while clicking logout button.")


    def get_loginpage_heading(self):
        text=self.driver.find_element(By.XPATH,self.login_page_heading).text
        return text

