import time

from selenium.webdriver.common.keys import Keys

from .locators import *
from DOM.pages import Page
from features.utils.helper_methods import *


class OnboardingPage(Page):
    def __abs__(self, context):
        Page.__init__(self, context)

    def fill_in_onboarding_data(self, name=None, last_name=None, postal_code=None, address=None):
        if not name:
            name = random_word(8)
        if not last_name:
            last_name = random_word(15)
        if not postal_code:
            postal_code = '28009'
        if not address:
            address = random_text(4)
        name_field = self.find_element_waiting(onboarding_form.name_field)
        name_field.send_keys(name, Keys.RETURN)

        last_name_field = self.find_element_by_locator(onboarding_form.last_name_filed)
        last_name_field.send_keys(last_name, Keys.RETURN)

        postal_code_field = self.find_element_by_locator(onboarding_form.postal_code_field)
        self.send_text_to_validated_field(postal_code_field, postal_code)

        address_field = self.find_element_waiting(onboarding_form.address_field)
        address_field.send_keys(address, Keys.RETURN)
        address_field.submit()

    @staticmethod
    def send_text_to_validated_field(webelement, text):
        webelement.send_keys(text, Keys.RETURN)
        time.sleep(0.5)
        webelement.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        webelement.send_keys(Keys.RETURN)

    def fill_in_package_info(self, weight=1, length=10, width=10, height=10):
        weight_field = self.find_element_waiting(onboarding_form.packet_weight)
        weight_field.send_keys(weight)

        length_field = self.find_element_by_locator(onboarding_form.packet_length)
        length_field.send_keys(length)

        width_field = self.find_element_by_locator(onboarding_form.packet_width)
        width_field.send_keys(width)

        height_field = self.find_element_by_locator(onboarding_form.packet_height)
        height_field.send_keys(height)

        height_field.submit()