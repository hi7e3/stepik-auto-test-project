from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "There are items in the basket, but should not be"
    
    def should_be_basket_empty_continue_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_CONTINUE), "No Empty Basket message"
