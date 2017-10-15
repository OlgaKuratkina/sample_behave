import time

import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from .locators import *


class Page:
    timeout_seconds = 10

    def __init__(self, context):
        self.context = context
        self.browser = context.browser
        self.actions = ActionChains(self.browser)

    def waiting(self, condition):
        wd = self.browser
        wait = ui.WebDriverWait(wd, 10)
        wait.until(lambda wd: condition)
        return condition

    def find_element_waiting(self, locator, many=False):
        number_tries = self.context.timeout_tries
        while number_tries > 0:
            try:
                element = self.find_element_by_locator(locator, many)
                return element
            except NoSuchElementException:
                number_tries -= 1
                time.sleep(0.5)

    def get_attribute_safe(self, locator, attribute):
        num_tries = self.context.timeout_tries
        title = None
        element = self.find_element_waiting(locator)
        for i in range(num_tries):
            title = element.get_attribute(attribute)
            if not title or title == '()':
                num_tries -= 1
                time.sleep(1)
        return title

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

    def goto_pro_page(self):
        self.browser.get(pro_page.url)

    def goto_register_page(self):
        self.browser.get(register_page.url)

    def goto_shipments_page(self):
        self.browser.get(create_sending_page.url)

    def safe_logout(self):
        try:
            logout = self.find_element_waiting(onboarding_page.logout)
        except NoSuchElementException or AttributeError:
            return
        if logout:
            logout.click()

    def scroll_down(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")

    def find_element_by_locator(self, locator, many=False):
        locator_type, locator_value = locator.split('=')
        if locator_type == 'class':
            if not many:
                return self.browser.find_element_by_class_name(locator_value)
            return self.browser.find_elements_by_class_name(locator_value)
        elif locator_type == 'css':
            if not many:
                return self.browser.find_element_by_css_selector(locator_value)
            return self.browser.find_elements_by_css_selector(locator_value)
        elif locator_type == 'id':
            if not many:
                return self.browser.find_element_by_id(locator_value)
            return self.browser.find_elements_by_id(locator_value)
        elif locator_type == 'link':
            if not many:
                return self.browser.find_element_by_link_text(locator_value)
            return self.browser.find_elements_by_link_text(locator_value)
        elif locator_type == 'name':
            if not many:
                return self.browser.find_element_by_name(locator_value)
            return self.browser.find_elements_by_name(locator_value)
        elif locator_type == 'plink':
            if not many:
                return self.browser.find_element_by_partial_link_text(locator_value)
            return self.browser.find_elements_by_partial_link_text(locator_value)
        elif locator_type == 'tag':
            if not many:
                return self.browser.find_element_by_tag_name(locator_value)
            return self.browser.find_elements_by_tag_name(locator_value)
        elif locator_type == 'xpath':
            if not many:
                return self.browser.find_element_by_xpath(locator_value)
            return self.browser.find_elements_by_xpath(locator_value)
        else:
            raise Exception('Invalid locator')


class CreateSendingPage(Page):
    def __abs__(self, context):
        Page.__init__(self, context)

