from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class StronaGlownaZalogowany:
    URL = 'http://localhost:8080/homeloged'
    KOMUNIKAT_TEKST = (By.ID 'message_login')


    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def stronaGlownaZalogowany(self):
        login_nav = self.browser.find_element(*self.NAV_LOGIN)
        login_nav.click()

    def checkLogedText(self, phrase):
        message = self.browser.find_element(*self.KOMUNIKAT_TEKST).text
        assert message == phrase
