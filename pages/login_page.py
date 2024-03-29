from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self,browser):
        assert "login" in self.browser.current_url, f"expected login to be substring of '{browser.current_url}'"

    def should_be_login_form(self):
        assert self.is_element_present (*LoginPageLocators.LOGIN_FORM_LINK), "Login form link is not presented"


    def should_be_register_form(self):
        assert self.is_element_present (*LoginPageLocators.REGISTER_FORM_LINK), "Register form link is not presented"
