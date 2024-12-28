from screenplay.ui.candidate_ui import CandidateUI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def validate_status(actor):
    wait = WebDriverWait(actor.browser, 10)
    return wait.until(EC.presence_of_element_located(CandidateUI.STATUS)).is_displayed()
