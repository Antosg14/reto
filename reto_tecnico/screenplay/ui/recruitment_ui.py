from selenium.webdriver.common.by import By

class RecruitmentUI:
    MENU = (By.XPATH, "//span[text()='Recruitment']")
    ADD_BUTTON = (By.XPATH, "//button[contains(., '+ Add')]")
