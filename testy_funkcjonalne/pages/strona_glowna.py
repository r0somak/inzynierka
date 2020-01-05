from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class StronaGlowna:
    URL = 'http://localhost:8080/'
    NAV_LOGIN = (By.LINK_TEXT, 'Logowanie')
    NAV_REGISTER = (By.LINK_TEXT, 'Rejestracja')


    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def stronaLogowania(self):
        login_nav = self.browser.find_element(*self.NAV_LOGIN)
        login_nav.click()

    def checkIfLogedOut(self):
        login_nav = self.browser.find_element(*self.NAV_LOGIN).text
        assert len(login_nav) > 0

    def stronaRejestracji(self):
        register_nav = self.browser.find_element(*self.NAV_REGISTER)
        register_nav.click()

    def checkIfRegistered(self):
         register_nav = self.browser.find_element(*self.NAV_REGISTER).text
         assert len(register_nav) > 0
