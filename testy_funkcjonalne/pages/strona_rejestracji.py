from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

class StronaRejestracji:
    URL = 'http://localhost:8080/register'
    POLE_LOGIN = (By.ID, 'login')
    POLE_EMAIL= (By.ID, 'email')
    POLE_HASLO = (By.ID, 'password')
    PRZYCISK_REJESTRACJA = (By.ID, 'button_register')
    HEAD_REGISTER = (By.XPATH, '/html/body/div/div/div[2]/p/b')
    ERROR_MESSAGE_LOGIN = (By.XPATH, '/html/body/div/div/div[2]/span/form/span[1]/span')
    ERROR_MESSAGE_EMAIL = (By.XPATH, '/html/body/div/div/div[2]/span/form/span[2]/span')
    ERROR_MESSAGE_PASSWORD = (By.XPATH, '/html/body/div/div/div[2]/span/form/span[3]/span')


    def __init__(self, browser):
        self.browser = browser

    def inputUsername(self, phrase):
        username_input = self.browser.find_element(*self.POLE_LOGIN)
        username_input.clear()
        username_input.send_keys(phrase)

    def inputEmail(self, phrase):
        email_input = self.browser.find_element(*self.POLE_EMAIL)
        email_input.clear()
        email_input.send_keys(phrase)

    def inputPassword(self, phrase):
        password_input = self.browser.find_element(*self.POLE_HASLO)
        password_input.clear()
        password_input.send_keys(phrase)

    def clickRegister(self):
        time.sleep(0.5)
        register_button = self.browser.find_element(*self.PRZYCISK_REJESTRACJA)
        register_button.click()

    def clickPage(self):
        time.sleep(0.5)
        head_register = self.browser.find_element(*self.HEAD_REGISTER)
        head_register.click()

    def checkIfErrorNoLoginExists(self):
        error_no_login = self.browser.find_element(*self.ERROR_MESSAGE_LOGIN).text
        assert len(error_no_login) > 0

    def checkIfErrorNoEmailExists(self):
        error_no_email = self.browser.find_element(*self.ERROR_MESSAGE_EMAIL).text
        assert len(error_no_email) > 0

    def checkIfErrorNoPasswordExists(self):
        error_no_password= self.browser.find_element(*self.ERROR_MESSAGE_PASSWORD).text
        assert len(error_no_password) > 0

    def checkIfInvalidLogin(self):
        invalid_login = self.browser.find_element(*self.ERROR_MESSAGE_LOGIN).text
        assert len(invalid_login) > 0

    def checkIfInvalidEmail(self):
        invalid_email = self.browser.find_element(*self.ERROR_MESSAGE_EMAIL).text
        assert len(invalid_email) > 0

    def checkIfInvalidPassword(self):
        invalid_password = self.browser.find_element(*self.ERROR_MESSAGE_PASSWORD).text
        assert len(invalid_password) > 0
