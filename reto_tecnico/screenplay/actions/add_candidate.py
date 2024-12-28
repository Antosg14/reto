from screenplay.ui.recruitment_ui import RecruitmentUI
from screenplay.ui.candidate_ui import CandidateUI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def add_candidate(actor, first_name, last_name, email):
    wait = WebDriverWait(actor.browser, 10)
    wait.until(EC.presence_of_element_located(RecruitmentUI.ADD_BUTTON)).click()
    
    wait.until(EC.presence_of_element_located(CandidateUI.FIRST_NAME)).send_keys(first_name)
    actor.browser.find_element(*CandidateUI.LAST_NAME).send_keys(last_name)
    actor.browser.find_element(*CandidateUI.EMAIL).send_keys(email)
    actor.browser.find_element(*CandidateUI.SAVE_BUTTON).click()
