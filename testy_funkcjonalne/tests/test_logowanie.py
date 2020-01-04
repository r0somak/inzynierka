import random
import string

import pytest
from pages.logowanie import StronaLogowania
from pages.strona_glowna import StronaGlowna
import credentials
from tests.initialize import browser, config, config_wait_time, config_browser

def randomString(stringLength = 5):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

@pytest.mark.usefixtures("browser", "config", "config_browser", "config_wait_time")
def test_poprawne_logowanie(browser):
    main_page = StronaGlowna(browser)
    main_page.load()
    main_page.stronaLogowania()

    login_page.inputUsername(credentials.LOGIN)
    login_page.inputPassword(credentials.PASSWORD)
    login_page.clickLogin()

    main_page_loged = StronaGlownaZalogowany(browser)
    main_page_loged.checkLogedText(StronaGlownaZalogowany.KOMUNIKAT_TEKST)

def test_brak_danych_logowania(browser):
    login_page = IbisStronaLogowania(browser)
    login_page.load()

    login_page.inputUsername('')
    login_page.inputPassword('')
    login_page.clickLogin()

    login_page.checkMessage(IbisStronaLogowania.KOMUNIKAT_BRAK_DANYCH)

def test_bledne_dane_logowania(browser):
    fakeCredential = randomString()

    login_page = IbisStronaLogowania(browser)
    login_page.load()

    login_page.inputUsername(fakeCredential)
    login_page.inputPassword(fakeCredential)
    login_page.clickLogin()

    login_page.checkMessage(IbisStronaLogowania.KOMUNIKAT_BLEDNE_DANE)

def test_brak_hasla(browser):
    fakeCredential = randomString()
    login_page = IbisStronaLogowania(browser)
    login_page.load()

    login_page.inputUsername(fakeCredential)
    login_page.clickLogin()

    login_page.checkMessage(IbisStronaLogowania.KOMUNIKAT_BRAK_HASLA)

def test_brak_loginu(browser):
    fakeCredential = randomString()
    login_page = IbisStronaLogowania(browser)
    login_page.load()

    login_page.inputPassword(fakeCredential)
    login_page.clickLogin()

    login_page.checkMessage(IbisStronaLogowania.KOMUNIKAT_BRAK_DANYCH)

def test_zablokowanie_usera(browser):
    fakeCredential = randomString(random.randint(5, 10))
    login_page = IbisStronaLogowania(browser)
    login_page.load()

    i = 0
    while i < IbisStronaLogowania.LOGIN_ATTEMPTS:
        login_page.inputUsername(fakeCredential)
        login_page.inputPassword(fakeCredential)
        login_page.clickLogin()
        i += 1

    login_page.checkMessage(IbisStronaLogowania.KOMUNIKAT_BLOKADA_UZYTKOWNIKA)

def test_poprawne_wylogowanie(browser):
    login_page = IbisStronaLogowania(browser)
    login_page.load()
    login_page.inputUsername(credentials.LOGIN)
    login_page.inputPassword(credentials.PASSWORD)
    login_page.clickLogin()

    search_page = IbisWyszukiwarka(browser)
    search_page.clickLogoutButton()

    login_page.checkTabName()
