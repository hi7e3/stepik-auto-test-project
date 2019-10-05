from selenium.webdriver.common.by import By


class MainPageLocators():
    pass
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_NAME_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-success > .alertinner > strong")
    PRODUCT_PRICE_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON_TOP = (By.CSS_SELECTOR, ".basket-mini a.btn")
    
class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_CONTINUE = (By.CSS_SELECTOR, "#content_inner > p > a")
