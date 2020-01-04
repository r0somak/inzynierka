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

    login_page = StronaLogowania(browser)
    login_page.inputUsername(credentials.LOGIN)
    login_page.inputPassword(credentials.PASSWORD)
    login_page.clickLogin()

    main_page_loged = StronaGlownaZalogowany(browser)
    main_page_loged.checkLogedText(StronaGlownaZalogowany.KOMUNIKAT_TEKST)








