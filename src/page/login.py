from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.__txt_user = "/html/body/div[2]/div[2]/div/div/section/div/div/div/div/form/div[1]/input"
        self.__txt_password = "/html/body/div[2]/div[2]/div/div/section/div/div/div/div/form/div[2]/input"
        self.__btn_login = "/html/body/div[2]/div[2]/div/div/section/div/div/div/div/form/div[3]/button"
        self.__wait = WebDriverWait(self.driver, 10)


    def input_username(self):
        
        field_username = self.__wait.until(
            EC.visibility_of_element_located((By.XPATH, self.__txt_user))
        )
        return field_username

    def input_password(self):
        field_password = self.__wait.until(
            EC.visibility_of_element_located((By.XPATH, self.__txt_password))
        )
        return field_password

    def button_login(self):
        return self.__wait.until(
            EC.visibility_of_element_located((By.XPATH, self.__btn_login))
        )
    

    def login(self, username, password):
        self.input_username().send_keys(username)
        self.input_password().send_keys(password)
        self.button_login().click()


    def valid_login(self, username, password):
        return self.login(username, password)
