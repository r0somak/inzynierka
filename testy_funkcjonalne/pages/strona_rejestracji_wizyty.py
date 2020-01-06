from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

class StronaRejestracjiWizyty:
    URL = 'http://localhost:8080/visit'
    POLE_DATA_CZAS = (By.ID, 'data')
    POLE_NOTE = (By.CLASS_NAME, 'uwagi')
    PRZYCHODNIA_OPTION = (By.ID, 'przychodnia')
    LEKARZ_OPTION = (By.ID, 'lekarz')
    OBJAWY_OPTION = (By.ID, 'objawy')
    PRZYCISK_REJESTRACJA_WIZYTY = (By.ID, 'button_visit')
    TOAST_MESSAGE = (By.CLASS_NAME, 'b-toaster-slot')


    def __init__(self, browser):
        self.browser = browser

    def inputDateTime(self, phrase):
        date_time_input = self.browser.find_element(*self.POLE_DATA_CZAS)
        date_time_input.clear()
        date_time_input.send_keys(phrase)

    def inputNote(self, phrase):
        note_input = self.browser.find_element(*self.POLE_NOTE)
        note_input.clear()
        note_input.send_keys(phrase)

    def selectMedicalCenter(self, phrase):
        select = Select(self.browser.find_element(*self.PRZYCHODNIA_OPTION))
        select.select_by_visible_text(phrase)

    def selectDoctor(self, phrase):
        select = Select(self.browser.find_element(*self.LEKARZ_OPTION))
        select.select_by_visible_text(phrase)

    def selectSympt(self, phrase):
        sympt_select = self.browser.find_element(*self.OBJAWY_OPTION)
        sympt_select.send_keys(phrase + Keys.ENTER)
        sympt_select.clear()


    def clickRegisterVisit(self):
        time.sleep(0.5)
        register_visit_button = self.browser.find_element(*self.PRZYCISK_REJESTRACJA_WIZYTY)
        register_visit_button.click()

    def checkIfInvalidDateTime(self):
        date_time_invalid = self.browser.find_element(*self.POLE_DATA_CZAS).getAttribute("validationMessage")
        print(date_time_invalid)



    def checkToastMessage(self):
        try:
            toast_message = self.browser.find_element(*self.TOAST_MESSAGE)
        except NoSuchElementException:
             return False
        return True

