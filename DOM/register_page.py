from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from .locators import *
from features.utils.helper_methods import *
from DOM.pages import Page


class RegisterPage(Page):
    def __abs__(self, context):
        Page.__init__(self, context)

    def login_user(self, email, password):
        email_field = self.waiting(self.find_element_by_locator(login_form.email_field))
        email_field.send_keys(email, Keys.ENTER)

        password_field = self.find_element_by_locator(login_form.password_field)
        password_field.send_keys(password, Keys.RETURN)

    def register_user(self, email, password=None, phone=None, sendings_index=1, shops_index=1, marketplace_index=1):
        if not password:
            password = random_password(10)
        if not phone:
            phone = random_phone()

        email_field = self.waiting(self.find_element_by_locator(register_form.email_field))
        email_field.clear()
        email_field.send_keys(email, Keys.RETURN)

        password_field = self.find_element_by_locator(register_form.password_field)
        password_field.clear()
        password_field.send_keys(password, Keys.RETURN)

        sendings_field = Select(self.find_element_by_locator(register_form.sendings_qty))
        sendings_field.select_by_index(sendings_index)

        shops_field = Select(self.find_element_by_locator(register_form.online_shops))
        shops_field.select_by_index(shops_index)

        marketplace_field = Select(self.find_element_by_locator(register_form.marketplace_shops))
        marketplace_field.select_by_index(marketplace_index)

        phone_field = self.find_element_by_locator(register_form.phone_field)
        phone_field.clear()
        phone_field.send_keys(phone)
        phone_field.submit()

