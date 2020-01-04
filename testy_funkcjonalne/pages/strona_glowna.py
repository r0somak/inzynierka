from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class StronaGlowna:
    URL = 'http://localhost:8080/'
    NAV_LOGIN = (By.LINK_TEXT, 'Logowanie')

    LOGIN_ATTEMPTS = 4

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def stronaLogowania(self):
        login_nav = self.browser.find_element(*self.NAV_LOGIN)
        login_nav.click()
