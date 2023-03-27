from selenium.webdriver.common.by import By



class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")