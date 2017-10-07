from behave import *
from features.utils.pages import Page
from features.utils.locators import *


@given('internet user is on start page')
def step_impl(context):
    page = Page(context)
    page.goto_base_page()
    print('I see the main header with moto')
    element = page.find_element_by_locator(base_page.header_moto)
    assert element


@when("user navigates Pro Packlink")
def step_impl(context):
    print('I navigate to register page')
    page = Page(context)
    page.find_element_by_locator(base_page.navigate_to_pro).click()


@when("user clicks on Register button")
def step_impl(context):
    print('I click register')
    page = Page(context)
    page.find_element_by_locator(register_page.register_button).click()
    assert page.browser.current_url.endswith(register_page.url)  # Check that we navigated to the correct address


@step("user sees the registration form with five fields")
def step_impl(context):
    print('I see the form')
    page = Page(context)
    email_field = page.find_element_by_locator(register_form.email_field)
    assert email_field
    password_field = page.find_element_by_locator(register_form.password_field)
    assert password_field
    sendings_field = page.find_element_by_locator(register_form.sendings_qty)
    assert sendings_field
    shops_field = page.find_element_by_locator(register_form.online_shops)
    assert shops_field
    marketplace_field = page.find_element_by_locator(register_form.marketplace_shops)
    assert marketplace_field
    phone_field = page.find_element_by_locator(register_form.phone_field)
    assert phone_field



# @when('we implement {number:d} tests')
# def step_impl(context, number):  # -- NOTE: number is converted into integer
#     assert number > 1 or number == 0
#     context.tests_count = number
#
# @then('behave will test them for us!')
# def step_impl(context):
#     assert context.failed is False
#     assert context.tests_count >= 0