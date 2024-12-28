from screenplay.ui.login_ui import LoginUI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(actor, username, password):
    wait = WebDriverWait(actor.browser, 10)
    wait.until(EC.presence_of_element_located(LoginUI.USERNAME)).send_keys(username)
    actor.browser.find_element(*LoginUI.PASSWORD).send_keys(password)
    actor.browser.find_element(*LoginUI.LOGIN_BUTTON).click()
