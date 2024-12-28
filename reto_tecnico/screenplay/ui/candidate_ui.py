from selenium.webdriver.common.by import By

class CandidateUI:
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    EMAIL = (By.XPATH, "//input[@type='email']")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")
    STATUS = (By.XPATH, "//div[text()='Hired']")
