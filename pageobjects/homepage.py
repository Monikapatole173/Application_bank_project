from selenium.webdriver.common.by import By


class HomePage:
    login_text_xpath = "//a[normalize-space()='Login']"
    signup_text_xpath = "//a[normalize-space()='Sign Up']"


    def __init__(self,driver):
        self.driver = driver

    def click_on_login(self):
        self.driver.find_element(By.XPATH,self.login_text_xpath).click()

    def click_on_signup(self):
        self.driver.find_element(By.XPATH, self.signup_text_xpath).click()




