import random
import string

import pytest
from pages.logowanie import StronaLogowania
from pages.strona_glowna import StronaGlowna
from pages.strona_glowna_zalogowany import StronaGlownaZalogowany
from pages.strona_rejestracji_wizyty import StronaRejestracjiWizyty
import credentials
from tests.initialize import browser, config, config_wait_time, config_browser

DATA_CZAS = '2021-10-30T10:34:56.000000Z'
PRZYCHODNIA = 'MEDYK'
DOKTOR = 'Mareczek Kłodka'
OBJAW1 = 'Kaszel'
OBJAW2 = 'powiększenie węzłów chłonnych'
OBJAW3 = 'Dreszcze'

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

def randomString(stringLength = 10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

@pytest.mark.usefixtures("browser", "config", "config_browser", "config_wait_time")
def test_rejestracja_wizyty(browser):
    poprawne_logowanie_pacjent(browser)

    main_page_loged = StronaGlownaZalogowany(browser)
    main_page_loged.clickUmowWizyte()

    register_visit_page = StronaRejestracjiWizyty(browser)

    register_visit_page.inputDateTime(DATA_CZAS)
    Note = randomString()
    register_visit_page.inputNote(Note)
    register_visit_page.selectMedicalCenter(PRZYCHODNIA)
    register_visit_page.selectDoctor(DOKTOR)
    register_visit_page.selectSympt(OBJAW1)
    register_visit_page.clickRegisterVisit()
    register_visit_page.checkToastMessage()










