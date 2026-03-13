from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import  expected_conditions as EC

class UserManagement:
    user_mgnt_heading_xpath="//h2[normalize-space()='User Management']"
    username_xpath="//input[@type='text']"
    search_user_button_xpath="//button[@type='submit']"
    create_user_button_xpath="//a[normalize-space()='Create User']"
    view_all_user_button_xpath="////a[normalize-space()='View All Users']"
    dashboard_xpath="//a[normalize-space()='Dashboard']"
    logout_xpath="//a[normalize-space()='Logout']"
    edit_user_title_xpath="//h2[normalize-space()='Edit User']"
    user_not_found_error_xpath="//div[normalize-space()='User not found']"
    user_mgnt_button_dashboard_xpath="//a[normalize-space()='User Management']"


    def __init__(self,driver):
        self.driver = driver

    def get_edit_user_page_heading(self):
        try:
            wait= WebDriverWait(self.driver,timeout=10)
            element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.edit_user_title_xpath)))
            return element.text
        except Exception as e:
            self.get_user_not_found_error()

    def get_user_not_found_error(self):
        try:
            wait= WebDriverWait(self.driver,timeout=10)
            element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.user_not_found_error_xpath)))
            return element.text
        except Exception as e:
            return False

    def get_user_mgnt_heading(self):
        try:
            wait= WebDriverWait(self.driver,timeout=10)
            element = wait.until(expected_conditions.visibility_of_element_located((By.XPATH,self.user_mgnt_heading_xpath)))
            return element.text
        except Exception as e:
            return False

    def set_search_username_field(self,username):
        wait = WebDriverWait(self.driver, 10)

        search_box = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='text']"))
        )

        search_box.send_keys(username)

    def click_search_user_button(self):
        try:
            wait= WebDriverWait(self.driver,timeout=5)
            element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,self.search_user_button_xpath)))
            self.driver.execute_script("arguments[0].click();", element)
            #element.click()
        except Exception as e:
            print(f"Error while clicking search user button")

    def click_create_user_button(self):
        try:
            wait= WebDriverWait(self.driver,timeout=5)
            element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,self.create_user_button_xpath)))
            self.driver.execute_script("arguments[0].click();", element)
            #element.click()
        except Exception as e:
            print(f"Error while clicking create user button")

    def click_view_all_user_button(self):
        try:
            wait= WebDriverWait(self.driver,timeout=5)
            element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,self.view_all_user_button_xpath)))
            self.driver.execute_script("arguments[0].click();", element)
            #element.click()
        except Exception as e:
            print(f"Error while clicking view all user button")

    def click_dashboard_button(self):
        try:
            wait= WebDriverWait(self.driver,timeout=5)
            element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,self.dashboard_xpath)))
            self.driver.execute_script("arguments[0].click();", element)
            #element.click()
        except Exception as e:
            print(f"Error while clicking dashboard button")

    def click_logout_button(self):
        try:
            wait= WebDriverWait(self.driver,timeout=10)
            element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,self.logout_xpath)))
            self.driver.execute_script("arguments[0].click();", element)
            #element.click()
        except Exception as e:
            print(f"Error while clicking logout button")


    def click_user_management_button(self):
        try:
            wait= WebDriverWait(self.driver,timeout=10)
            element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH,self.user_mgnt_button_dashboard_xpath)))
            self.driver.execute_script("arguments[0].click();", element)
            #element.click()
        except Exception as e:
            print(f"Error while clicking user management dashboard button")


