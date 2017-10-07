import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

from .locators import *
from features.utils.helper_methods import *


class Page:
    timeout_seconds = 10

    def __init__(self, context):
        self.browser = context.browser

    def waiting(self, condition):
        wd = self.browser
        wait = ui.WebDriverWait(wd, 10)
        wait.until(lambda wd: condition)
        return condition

    def find_element_waiting(self, locator):
        number_tries = 10
        while number_tries > 0:
            try:
                element = self.find_element_by_locator(locator)
                return element
            except:
                number_tries -= 1
                time.sleep(1)

    # def waiting_invisible(self, element_id):
    #     driver = self.browser
    #     try:
    #         element = WebDriverWait(driver, 10).until(
    #             EC.visibility_of_element_located((By.ID, element_id)))
    #         return element
    #     finally:
    #         return None

    def goto_base_page(self):
        self.browser.get(base_page.url)

    def goto_register_page(self):
        self.browser.get(register_page.url)

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")

    def find_element_by_locator(self, locator):
        locator_type, locator_value = locator.split('=')
        if locator_type == 'class':
            return self.browser.find_element_by_class_name(locator_value)
        elif locator_type == 'css':
            return self.browser.find_element_by_css_selector(locator_value)
        elif locator_type == 'id':
            return self.browser.find_element_by_id(locator_value)
        elif locator_type == 'link':
            return self.browser.find_element_by_link_text(locator_value)
        elif locator_type == 'name':
            return self.browser.find_element_by_name(locator_value)
        elif locator_type == 'plink':
            return self.browser.find_element_by_partial_link_text(locator_value)
        elif locator_type == 'tag':
            return self.browser.find_element_by_tag_name(locator_value)
        elif locator_type == 'xpath':
            return self.browser.find_element_by_xpath(locator_value)
        else:
            raise Exception('Invalid locator')


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
        phone_field.send_keys(phone, Keys.RETURN)
        phone_field.submit()


class OnboardingPage(Page):
    def __abs__(self, context):
        Page.__init__(self, context)

    def fill_in_onboarding_data(self, name=None, last_name=None, postal_code=None, address=None):
        if not name:
            name = random_word(8)
        if not last_name:
            last_name = random_word(15)
        if not postal_code:
            postal_code = '21007'
        if not address:
            address = random_text(4)
        name_field = self.find_element_waiting(onboarding_form.name_field)
        name_field.send_keys(name, Keys.RETURN)

        last_name_field = self.find_element_by_locator(onboarding_form.last_name_filed)
        last_name_field.send_keys(last_name, Keys.RETURN)

        postal_code_field = self.find_element_by_locator(onboarding_form.postal_code_field)
        postal_code_field.send_keys(postal_code, Keys.RETURN)
        time.sleep(0.5)
        postal_code_field.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        postal_code_field.send_keys(Keys.RETURN)

        address_field = self.find_element_waiting(onboarding_form.address_field)
        address_field.send_keys(address, Keys.RETURN)
        address_field.submit()
