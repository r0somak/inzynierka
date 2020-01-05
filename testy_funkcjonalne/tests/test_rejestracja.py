import random
import string

import pytest
from pages.logowanie import StronaLogowania
from pages.strona_glowna import StronaGlowna
from pages.strona_glowna_zalogowany import StronaGlownaZalogowany
from pages.strona_rejestracji import StronaRejestracji
import credentials
from tests.initialize import browser, config, config_wait_time, config_browser


def randomString(stringLength = 7):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def randomEmail(stringLength = 1):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength)).join('test@wp.pl')

def randomError(stringLength = 1):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

@pytest.mark.usefixtures("browser", "config", "config_browser", "config_wait_time")
def test_poprawna_rejestracja(browser):
    main_page = StronaGlowna(browser)
    main_page.load()
    main_page.stronaRejestracji()

    register_page = StronaRejestracji(browser)
    fakeCredential = randomString()
    fakeEmail = randomEmail()
    register_page.inputUsername(fakeCredential)
    register_page.inputEmail(fakeEmail)
    register_page.inputPassword(fakeCredential)
    register_page.clickRegister()
    main_page.checkIfRegistered()

def test_brak_danych_rejestracji(browser):
    main_page = StronaGlowna(browser)
    main_page.load()
    main_page.stronaRejestracji()

    register_page = StronaRejestracji(browser)
    register_page.inputUsername('')
    register_page.inputEmail('')
    register_page.inputPassword('')
    register_page.clickPage()
    register_page.clickRegister()
    register_page.checkIfErrorNoLoginExists()
    register_page.checkIfErrorNoEmailExists()
    register_page.checkIfErrorNoPasswordExists()


def test_bledne_dane_rejestracji(browser):
    main_page = StronaGlowna(browser)
    main_page.load()
    main_page.stronaRejestracji()

    register_page = StronaRejestracji(browser)
    fakeCredentialsError = randomError()
    register_page.inputUsername(fakeCredentialsError)
    register_page.inputEmail(fakeCredentialsError)
    register_page.inputPassword(fakeCredentialsError)
    register_page.clickRegister()
    register_page.checkIfInvalidLogin()
    register_page.checkIfInvalidEmail()
    register_page.checkIfInvalidPassword()







