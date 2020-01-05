import random
import string

import pytest
from pages.logowanie import StronaLogowania
from pages.strona_glowna import StronaGlowna
from pages.strona_glowna_zalogowany import StronaGlownaZalogowany
import credentials
from tests.initialize import browser, config, config_wait_time, config_browser

TEXT_LOGED_DOC = 'Jesteś zalogowany jako ' + credentials.LOGIN_DOC

def randomString(stringLength = 5):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

@pytest.mark.usefixtures("browser", "config", "config_browser", "config_wait_time")
def test_poprawne_logowanie_pacjent(browser):
    main_page = StronaGlowna(browser)
    main_page.load()
    main_page.stronaLogowania()

    login_page = StronaLogowania(browser)
    login_page.inputUsername(credentials.LOGIN)
    login_page.inputPassword(credentials.PASSWORD)
    login_page.clickLogin()

    main_page_loged = StronaGlownaZalogowany(browser)
    main_page_loged.checkIfLoged(StronaGlownaZalogowany.NAV_WIZYTA)

def test_poprawne_logowanie_lekarz(browser):
    main_page = StronaGlowna(browser)
    main_page.load()
    main_page.stronaLogowania()

    login_page = StronaLogowania(browser)
    login_page.inputUsername(credentials.LOGIN_DOC)
    login_page.inputPassword(credentials.PASSWORD_DOC)
    login_page.clickLogin()

    main_page_loged = StronaGlownaZalogowany(browser)
    main_page_loged.checkIfLogedDoc(TEXT_LOGED_DOC)

def test_brak_danych_logowania(browser):
    main_page = StronaGlowna(browser)
    main_page.load()
    main_page.stronaLogowania()

    login_page = StronaLogowania(browser)
    login_page.inputUsername('')
    login_page.inputPassword('')
    login_page.clickPage()
    login_page.checkIfErrorNoLoginExists()
    login_page.checkIfErrorNoPasswordExists()


def test_bledne_dane_logowania(browser):
    main_page = StronaGlowna(browser)
    main_page.load()
    main_page.stronaLogowania()

    login_page = StronaLogowania(browser)
    fakeCredential = randomString()
    login_page.inputUsername(fakeCredential)
    login_page.inputPassword(fakeCredential)
    login_page.clickLogin()
    login_page.checkToastMessage()


def test_poprawne_wylogowanie(browser):
    main_page = StronaGlowna(browser)
    main_page.load()
    main_page.stronaLogowania()

    login_page = StronaLogowania(browser)
    login_page.inputUsername(credentials.LOGIN)
    login_page.inputPassword(credentials.PASSWORD)
    login_page.clickLogin()

    main_page_loged = StronaGlownaZalogowany(browser)
    main_page_loged.checkIfLoged(StronaGlownaZalogowany.NAV_WIZYTA)

    main_page_loged.clickDropdown()
    main_page_loged.clickLogOut()

    main_page.checkIfLogedOut()






