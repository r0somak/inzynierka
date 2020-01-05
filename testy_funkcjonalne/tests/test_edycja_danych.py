import random
import string

import pytest
from pages.logowanie import StronaLogowania
from pages.strona_glowna import StronaGlowna
from pages.strona_glowna_zalogowany import StronaGlownaZalogowany
from pages.strona_edycji_danych_pacjenta import StronaEdycjiDanychPacjenta
import credentials
from tests.initialize import browser, config, config_wait_time, config_browser

NAME = 'Ola'
SURNAME = 'Bartos'
PESEL = '12345678900'
STREET = 'Judyma'
NUM_STREET = '60'
NUM_AP = ''
POST_CODE = ''
TOWN = 'Lublin'
PROVINCE = 'Lubelskie'
PHONE_NUM = '765809123'

VALID_NAME = 'Ol'
VALID_SURNAME = 'Ba'
VALID_PESEL = '12345'
VALID_STREET = 'Ju'
VALID_NUM_STREET = 'W'
VALID_NUM_AP = 'A'
VALID_POST_CODE = 'AA'
VALID_TOWN = 'Lu'
VALID_PROVINCE = 'Lubelskie'
VALID_PHONE_NUM = '765809'

def poprawne_logowanie_pacjent(browser):
    main_page = StronaGlowna(browser)
    main_page.load()
    main_page.stronaLogowania()

    login_page = StronaLogowania(browser)
    login_page.inputUsername(credentials.LOGIN)
    login_page.inputPassword(credentials.PASSWORD)
    login_page.clickLogin()

    main_page_loged = StronaGlownaZalogowany(browser)
    main_page_loged.checkIfLoged(StronaGlownaZalogowany.NAV_WIZYTA)

def randomString(stringLength = 7):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

@pytest.mark.usefixtures("browser", "config", "config_browser", "config_wait_time")
def test_poprawna_edycja_danych(browser):
    poprawne_logowanie_pacjent(browser)

    main_page_loged = StronaGlownaZalogowany(browser)
    main_page_loged.clickDropdown()
    main_page_loged.clickEdit()

    edit_page_pat = StronaEdycjiDanychPacjenta(browser)
    edit_page_pat.inputName(NAME)
    edit_page_pat.inputSurname(SURNAME)
    edit_page_pat.inputPesel(PESEL)
    edit_page_pat.inputStreet(STREET)
    edit_page_pat.inputNumStreet(NUM_STREET)
    edit_page_pat.inputNumAp(NUM_AP)
    edit_page_pat.inputPostCode(POST_CODE)
    edit_page_pat.inputTown(TOWN)
    edit_page_pat.inputProvince(PROVINCE)
    edit_page_pat.inputPhoneNum(PHONE_NUM)
    edit_page_pat.clickEdit()

def test_bledne_dane_edycji(browser):
    poprawne_logowanie_pacjent(browser)

    main_page_loged = StronaGlownaZalogowany(browser)
    main_page_loged.clickDropdown()
    main_page_loged.clickEdit()

    edit_page_pat = StronaEdycjiDanychPacjenta(browser)
    edit_page_pat.inputName(VALID_NAME)
    edit_page_pat.inputSurname(VALID_SURNAME)
    edit_page_pat.inputPesel(VALID_PESEL)
    edit_page_pat.inputStreet(VALID_STREET)
    edit_page_pat.inputNumStreet(VALID_NUM_STREET)
    edit_page_pat.inputNumAp(VALID_NUM_AP)
    edit_page_pat.inputPostCode(VALID_POST_CODE)
    edit_page_pat.inputTown(VALID_TOWN)
    edit_page_pat.inputProvince(VALID_PROVINCE)
    edit_page_pat.inputPhoneNum(VALID_PHONE_NUM)
    edit_page_pat.checkIfValidName()
    edit_page_pat.checkIfValidSurname()
    edit_page_pat.checkIfValidPesel()
    edit_page_pat.checkIfValidStreet()
    edit_page_pat.checkIfValidNumStreet()
    edit_page_pat.checkIfValidNumAp()
    edit_page_pat.checkIfValidPostCode()
    edit_page_pat.checkIfValidTown()
    edit_page_pat.checkIfValidPhoneNum()







