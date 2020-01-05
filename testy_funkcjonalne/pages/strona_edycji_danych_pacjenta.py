from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from selenium.webdriver.support.select import Select

class StronaEdycjiDanychPacjenta:
    URL = 'http://localhost:8080/editprofile'
    POLE_NAME = (By.ID, 'name')
    POLE_SURNAME = (By.ID, 'surname')
    POLE_PESEL = (By.ID, 'pesel')
    POLE_STREET = (By.ID, 'street')
    POLE_NUM_STREET = (By.ID, 'num_street')
    POLE_NUM_AP = (By.ID, 'num_ap')
    POLE_POST_CODE = (By.ID, 'post_code')
    POLE_TOWN = (By.ID, 'town')
    POLE_PROVINCE = (By.ID, 'province')
    POLE_PHONE_NUM = (By.ID, 'phone_num')
    PRZYCISK_EDYCJI = (By.ID, 'button_edit')
    TOAST_MESSAGE = (By.CLASS_NAME, 'b-toaster-slot')
    VALID_NAME = (By.XPATH, '/html/body/div[1]/div/div[2]/form[2]/span[1]/span')
    VALID_SURNAME = (By.XPATH, '/html/body/div[1]/div/div[2]/form[2]/span[2]/span')
    VALID_PESEL = (By.XPATH, '/html/body/div[1]/div/div[2]/form[2]/span[3]/span')
    VALID_STREET = (By.XPATH, '/html/body/div[1]/div/div[2]/form[2]/span[4]/span')
    VALID_NUM_STREET = (By.XPATH, '/html/body/div[1]/div/div[2]/form[2]/span[5]/span')
    VALID_NUM_AP = (By.XPATH, '/html/body/div[1]/div/div[2]/form[2]/span[6]/span')
    VALID_POST_CODE = (By.XPATH, '/html/body/div[1]/div/div[2]/form[2]/span[7]/span')
    VALID_TOWN = (By.XPATH, '/html/body/div[1]/div/div[2]/form[2]/span[8]/span')
    VALID_PHONE_NUM = (By.XPATH, '/html/body/div[1]/div/div[2]/form[2]/span[9]/span')
    HEAD_REGISTER = (By.XPATH, '/html/body/div/div/div[2]/p/b')
    ERROR_MESSAGE_LOGIN = (By.XPATH, '/html/body/div/div/div[2]/span/form/span[1]/span')
    ERROR_MESSAGE_EMAIL = (By.XPATH, '/html/body/div/div/div[2]/span/form/span[2]/span')
    ERROR_MESSAGE_PASSWORD = (By.XPATH, '/html/body/div/div/div[2]/span/form/span[3]/span')


    def __init__(self, browser):
        self.browser = browser

    def inputName(self, phrase):
        name_input = self.browser.find_element(*self.POLE_NAME)
        name_input.send_keys(Keys.CONTROL,"a", Keys.DELETE)
        name_input.send_keys(phrase)

    def inputSurname(self, phrase):
        surname_input = self.browser.find_element(*self.POLE_SURNAME)
        surname_input.send_keys(Keys.CONTROL,"a", Keys.DELETE)
        surname_input.send_keys(phrase)

    def inputPesel(self, phrase):
        pesel_input = self.browser.find_element(*self.POLE_PESEL)
        pesel_input.send_keys(Keys.CONTROL,"a", Keys.DELETE)
        pesel_input.send_keys(phrase)

    def inputStreet(self, phrase):
        street_input = self.browser.find_element(*self.POLE_STREET)
        street_input.send_keys(Keys.CONTROL,"a", Keys.DELETE)
        street_input.send_keys(phrase)

    def inputNumStreet(self, phrase):
        num_street_input = self.browser.find_element(*self.POLE_NUM_STREET)
        num_street_input.send_keys(Keys.CONTROL,"a", Keys.DELETE)
        num_street_input.send_keys(phrase)

    def inputNumAp(self, phrase):
        num_ap_input = self.browser.find_element(*self.POLE_NUM_AP)
        num_ap_input.send_keys(Keys.CONTROL,"a", Keys.DELETE)
        num_ap_input.send_keys(phrase)

    def inputPostCode(self, phrase):
        post_code_input = self.browser.find_element(*self.POLE_POST_CODE)
        post_code_input.send_keys(Keys.CONTROL,"a", Keys.DELETE)
        post_code_input.send_keys(phrase)

    def inputTown(self, phrase):
        town_input = self.browser.find_element(*self.POLE_TOWN)
        town_input.send_keys(Keys.CONTROL,"a", Keys.DELETE)
        town_input.send_keys(phrase)

    def inputProvince(self, phrase):
        select = Select(self.browser.find_element(*self.POLE_PROVINCE))
        select.select_by_visible_text(phrase)

    def inputPhoneNum(self, phrase):
        phone_num_input = self.browser.find_element(*self.POLE_PHONE_NUM)
        phone_num_input.send_keys(Keys.CONTROL,"a", Keys.DELETE)
        phone_num_input.send_keys(phrase)

    def clickEdit(self):
        time.sleep(0.5)
        edit_button = self.browser.find_element(*self.PRZYCISK_EDYCJI)
        edit_button.click()

    def checkToastMessage(self):
        try:
            toast_message = self.browser.find_element(*self.TOAST_MESSAGE)
        except NoSuchElementException:
             return False
        return True

    def checkIfValidName(self):
        valid_name = self.browser.find_element(*self.VALID_NAME).text
        assert len(valid_name) > 0

    def checkIfValidSurname(self):
        valid_surname = self.browser.find_element(*self.VALID_SURNAME).text
        assert len(valid_surname) > 0

    def checkIfValidPesel(self):
        valid_pesel = self.browser.find_element(*self.VALID_PESEL).text
        assert len(valid_pesel) > 0

    def checkIfValidStreet(self):
        valid_street = self.browser.find_element(*self.VALID_STREET).text
        assert len(valid_street) > 0

    def checkIfValidNumStreet(self):
        valid_num_street = self.browser.find_element(*self.VALID_NUM_STREET).text
        assert len(valid_num_street) > 0

    def checkIfValidNumAp(self):
        valid_num_ap = self.browser.find_element(*self.VALID_NUM_AP).text
        assert len(valid_num_ap) > 0

    def checkIfValidPostCode(self):
        valid_post_code = self.browser.find_element(*self.VALID_POST_CODE).text
        assert len(valid_post_code) > 0

    def checkIfValidTown(self):
        valid_town = self.browser.find_element(*self.VALID_TOWN).text
        assert len(valid_town) > 0

    def checkIfValidPhoneNum(self):
        valid_phone_num = self.browser.find_element(*self.VALID_PHONE_NUM).text
        assert len(valid_phone_num) > 0
