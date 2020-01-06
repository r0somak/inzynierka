from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class StronaGlownaZalogowany:
    URL = 'http://localhost:8080/homeloged'
    NAV_WIZYTA = (By.LINK_TEXT, 'Umów wizytę')
    PRZYCISK_WYLOGOWANIE = (By.ID, 'button_logout')
    NAV_TWOJE_KONTO = (By.ID, 'drop_text')
    TEXT_LOGED = (By.ID, 'message_login')
    PRZYCISK_EDYCJA_DANYCH = (By.LINK_TEXT, 'Edytuj dane')


    def __init__(self, browser):
        self.browser = browser

    def checkIfLoged(self, phrase):
        login_nav = self.browser.find_element(*self.NAV_WIZYTA).text
        assert len(login_nav) > 0

    def clickDropdown(self):
          dropdown_list = self.browser.find_element(*self.NAV_TWOJE_KONTO)
          dropdown_list.click()

    def clickLogOut(self):
         loginout_button = self.browser.find_element(*self.PRZYCISK_WYLOGOWANIE)
         loginout_button.click()

    def checkIfLogedDoc(self, phrase):
        loged_text = self.browser.find_element(*self.TEXT_LOGED).text
        print(phrase)
        assert phrase == loged_text

    def clickUmowWizyte(self):
        umow_wizyte = self.browser.find_element(*self.NAV_WIZYTA)
        umow_wizyte.click()

    def clickEdit(self):
         edit_button = self.browser.find_element(*self.PRZYCISK_EDYCJA_DANYCH)
         edit_button.click()
