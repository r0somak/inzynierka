from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

class StronaLogowania:
    URL = 'http://localhost:8080/login'
    POLE_LOGIN = (By.ID, 'login')
    POLE_HASLO = (By.ID, 'password')
    PRZYCISK_LOGOWANIE = (By.ID, 'button_login')
    ERROR_MESSAGE_LOGIN = (By.XPATH, '/html/body/div/div/div[2]/span/form/span[1]/span')
    HEAD_LOG = (By.XPATH, '/html/body/div/div/div[2]/p/b')
    ERROR_MESSAGE_PASSWORD = (By.XPATH, '/html/body/div/div/div[2]/span/form/span[2]/span')
    TOAST_MESSAGE = (By.CLASS_NAME, 'b-toaster-slot')


    def __init__(self, browser):
        self.browser = browser

    def inputUsername(self, phrase):
        username_input = self.browser.find_element(*self.POLE_LOGIN)
        username_input.clear()
        username_input.send_keys(phrase)

    def inputPassword(self, phrase):
        password_input = self.browser.find_element(*self.POLE_HASLO)
        password_input.clear()
        password_input.send_keys(phrase)


    def clickLogin(self):
        time.sleep(0.5)
        login_button = self.browser.find_element(*self.PRZYCISK_LOGOWANIE)
        login_button.click()

    def clickPage(self):
         time.sleep(0.5)
         login_button = self.browser.find_element(*self.HEAD_LOG)
         login_button.click()

    def checkIfErrorNoLoginExists(self):
        error_no_login = self.browser.find_element(*self.ERROR_MESSAGE_LOGIN).text
        assert len(error_no_login) > 0

    def checkIfErrorNoPasswordExists(self):
         error_no_login = self.browser.find_element(*self.ERROR_MESSAGE_PASSWORD).text
         assert len(error_no_login) > 0

    def checkToastMessage(self):
        try:
            toast_message = self.browser.find_element(*self.TOAST_MESSAGE)
        except NoSuchElementException:
             return False
        return True

