import pytest
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
link_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_reg_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, login_reg_link)
        page.open()
        new_email = str(time.time()) + "@fakeemail.org"
        page.register_new_user(new_email, "verylongpassword")
        page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        prod_name = page.get_product_name()
        prod_price = page.get_product_price()
        page.press_add_to_basket()
        page.should_basket_name_be_equal_product_name(prod_name)
        page.should_basket_price_be_equal_product_price(prod_price)


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link_promo)
    page.open()
    prod_name = page.get_product_name()
    prod_price = page.get_product_price()
    page.press_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_basket_name_be_equal_product_name(prod_name)
    page.should_basket_price_be_equal_product_price(prod_price)
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_promo)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail(reason="this test should fail: success message should be present")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.press_add_to_basket()
    page.should_not_be_success_message() 

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail(reason="this test should fail: success message should not disappear")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.press_add_to_basket()
    page.should_disappear_success_message()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_basket_empty_continue_message()
