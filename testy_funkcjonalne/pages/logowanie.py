from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class StronaLogowania:
    URL = 'http://localhost:8080/login'
    POLE_LOGIN = (By.NAME, 'Login')
    POLE_HASLO = (By.NAME, 'Hasło')
    PRZYCISK_LOGOWANIE = (By.ID, 'button_login')
    KOMUNIKAT_TEKST = (By.ID, 'message_login')

    KOMUNIKAT_BRAK_DANYCH = 'Podaj nazwę użytkownika i hasło'
    KOMUNIKAT_BLEDNE_DANE = 'Nieprawidłowa nazwa użytkownika lub hasło'
    KOMUNIKAT_BRAK_HASLA = 'Musisz podać hasło'
    KOMUNIKAT_BLOKADA_UZYTKOWNIKA = 'Konto zostało tymczasowo zablokowane.'
    ZAKLADKA_NAZWA = 'Zaloguj się'

    LOGIN_ATTEMPTS = 4

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
        login_button = self.browser.find_element(*self.PRZYCISK_LOGOWANIE)
        login_button.click()


    def checkTabName(self):
        tab_name = self.browser.title
        assert tab_name == self.ZAKLADKA_NAZWA
