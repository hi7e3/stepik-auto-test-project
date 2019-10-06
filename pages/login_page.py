from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        form_email = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        form_email.send_keys(email)
        form_pw1 = self.browser.find_element(*LoginPageLocators.PASSWORD1_INPUT)
        form_pw1.send_keys(email)
        form_pw2 = self.browser.find_element(*LoginPageLocators.PASSWORD2_INPUT)
        form_pw2.send_keys(email)
        form_register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        form_register_button.click()
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"