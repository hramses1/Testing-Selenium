from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class SiteAdministrator:
    def __init__(self, driver):
        self.driver = driver
        self.__btn_all_site_administrator = 'Más'
        self.__btn_site_administrator = "Administración del sitio"
        self.__btn_users= "/html/body/div[3]/div[3]/div/div[2]/div[1]/nav/ul/li[2]/a"
        self.__btn_browse_user_list = "/html/body/div[3]/div[3]/div/div[2]/div[2]/div/section/div/div/div[2]/div/div[2]/div[2]/ul/li[1]/a"
        self.__wait = WebDriverWait(self.driver, 10)


    def input_site_administrator(self):
        self.__wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, self.__btn_all_site_administrator))
        ).click()

        click = self.__wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, self.__btn_site_administrator ))
        )
        return click

    def input_users(self):
        click = self.__wait.until(
            EC.visibility_of_element_located((By.XPATH, self.__btn_users))
        )
        return click

    def browse_user_list(self):
        click= self.__wait.until(
            EC.visibility_of_element_located((By.XPATH, self.__btn_browse_user_list))
        )
        return click
    

    def result(self):
        self.input_site_administrator().click()
        self.input_users().click()
        self.browse_user_list().click()
        