from .locators import *


class Page:
    timeout_seconds = 10

    def __init__(self, context):
        self.browser = context.browser

    def goto_base_page(self):
        self.browser.get(base_page.url)

    def goto_register_page(self):
        self.browser.get(register_page.url)

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
