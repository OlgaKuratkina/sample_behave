from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


from .locators import *
from DOM.pages import Page
from DOM.onboarding_page import OnboardingPage


class SearchPage(OnboardingPage,Page):
    def __abs__(self, context):
        Page.__init__(self, context)

    def choose_create_new_sending(self):
        create_search_list = self.find_element_waiting(search_page.create_sending_list)
        self.actions.move_to_element(create_search_list).perform()
        create_search = self.find_element_waiting(search_page.create_sending)
        self.actions.move_to_element(create_search).click(create_search).perform()

    def search_for_sending(self, address, destination_address, weight, length, width, height):
        title = self.get_attribute_safe(search_page.predefined_address, 'title')
        print(address.lower(), title.lower())
        assert address.lower() in title.lower()

        destination = self.find_element_by_locator(search_page.postal_code)
        self.send_text_to_validated_field(destination, destination_address)
        self.scroll_down()
        package_select = self.find_element_waiting(search_page.package_selector)
        package_select.click()
        package_editable = self.find_element_waiting(search_page.editable_package)
        package_editable.click()

        self.fill_in_package_info(weight, length, width, height)

    def delete_predefined_address(self):
        try:
            change_address = self.find_element_waiting(search_page.change_address_button)
        except NoSuchElementException:
            return
        assert change_address
        change_address.click()
        try:
            popover = self.find_element_waiting(search_page.popover_div)
            self.actions.move_to_element(popover)
            self.actions.click_and_hold(popover)
            self.actions.send_keys(Keys.PAGE_DOWN)
            self.actions.perform()

            new_addess = self.find_element_waiting(search_page.new_address_button)
            self.actions.move_to_element(new_addess)
            self.actions.context_click(new_addess)
            self.actions.perform()
        except NoSuchElementException:
            return
        assert new_addess
        new_addess.click()

