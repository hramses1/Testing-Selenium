from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from common.fake_data import FakeData
import re

class CreateNewUser:
    def __init__(self, driver):
        self.driver = driver
        self.fake_data = FakeData()
        self.__btn_create_new_user = "/html/body/div[3]/div[4]/div/div[2]/div[2]/div/section/div/div[2]/form/button"
        self.__text_username= "id_username"
        self.__text_last_name= "id_firstname"
        self.__text_first_name= "id_lastname"
        self.__text_email = "id_email"
        self.__btn_password = "/html/body/div[4]/div[4]/div/div[2]/div[2]/div/section/div/form/fieldset[1]/div[2]/div[5]/div[2]/span/a[1]/span/span/em"
        self.__text_password = "id_newpassword"
        self.__text_city = "id_city"
        self.__text_country = "id_country"
        self.__text_description = "id_description_editoreditable"
        self.__btn_create_user= "id_submitbutton"
        self.__wait = WebDriverWait(self.driver, 20)


    def input_create_new_user(self):
        click = self.__wait.until(
            EC.visibility_of_element_located((By.XPATH, self.__btn_create_new_user))
        )
        return click

    def input_username(self):
        username = self.__wait.until(
            EC.visibility_of_element_located((By.ID, self.__text_username))
        )
        return username
    
    def input_first_name(self):
        first_name = self.__wait.until(
            EC.visibility_of_element_located((By.ID, self.__text_first_name))
        )
        return first_name
    
    def input_last_name(self):
        last_name = self.__wait.until(
            EC.visibility_of_element_located((By.ID, self.__text_last_name))
        )
        return last_name

    def input_email(self):
        email = self.__wait.until(
            EC.visibility_of_element_located((By.ID, self.__text_email))
        )
        return email

    def input_password(self):
        password = self.__wait.until(
            EC.visibility_of_element_located((By.XPATH, self.__btn_password))
        ).click()
        password_text= self.__wait.until(
            EC.visibility_of_element_located((By.ID, self.__text_password))
        )
        return password_text

    def input_city(self):
        city = self.__wait.until(
            EC.visibility_of_element_located((By.ID, self.__text_city))
        )
        return city

    def input_country(self):
        country = self.__wait.until(
            EC.visibility_of_element_located((By.ID, self.__text_country))
        )
        return country

    def input_description(self):
        description = self.__wait.until(
            EC.visibility_of_element_located((By.ID, self.__text_description))
        )
        return description
    
    def btn_create_user(self):
        btn_create_user = self.__wait.until(
            EC.visibility_of_element_located((By.ID, self.__btn_create_user))
        )
        return btn_create_user
    
        
    def add_information(self):
        username_field = self.input_username()
        user = re.sub(r"[^a-zA-Z0-9\s]", "",f'{self.fake_data.generate_person_data()["first_name"]}.{self.fake_data.generate_person_data()["last_name"]}'.lower())
        username_field.send_keys(user)
        
        first_name_field = self.input_first_name()
        first_name_field.send_keys(self.fake_data.generate_person_data()["first_name"])
        
        last_name_field = self.input_last_name()
        last_name_field.send_keys(self.fake_data.generate_person_data()["last_name"])
        
        email_field = self.input_email()
        email_field.send_keys(self.fake_data.generate_person_data()["email"])
        
        password_field = self.input_password()
        password_field.send_keys(self.fake_data.generate_person_data()["password"])
        
        city_field = self.input_city()
        city_field.send_keys(self.fake_data.generate_person_data()["city"])
        
        country_field = self.input_country()
        select_obj = Select(country_field)
        select_obj.select_by_visible_text(self.fake_data.generate_person_data()["country"])
        
        description_field = self.input_description()
        description_field.send_keys(self.fake_data.generate_person_data()["description"])
        
        btn_create_user = self.btn_create_user()
        btn_create_user.click()
        
        print(f'{self.fake_data.generate_person_data()}\n')
    def result(self):
        self.input_create_new_user().click()
        self.add_information()
        return True
