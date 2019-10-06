from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def press_add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()

    def get_product_name(self):
        prodname_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return(prodname_element.text)

    def get_product_price(self):
        prodprice_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return(prodprice_element.text)

    def should_basket_name_be_equal_product_name(self, pr_name):
        prodname_basket_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET_MESSAGE)
        assert pr_name == prodname_basket_element.text

    def should_basket_price_be_equal_product_price(self, pr_price):
        prodprice_basket_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET_MESSAGE)
        assert pr_price == prodprice_basket_element.text
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
    
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message has not disappeared, but should have"
