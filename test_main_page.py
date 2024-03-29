from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

def test_guest_should_see_login_in_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url(browser)

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_form_link(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_guest_should_see_register_form_link(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

