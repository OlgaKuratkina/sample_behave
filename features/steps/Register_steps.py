from behave import *

from DOM.pages import Page
from DOM.register_page import RegisterPage
from DOM.locators import *

from features.utils.helper_methods import random_password


@given('internet user is on start page')
def step_impl(context):
    page = Page(context)
    page.goto_base_page()
    element = page.find_element_waiting(base_page.header_moto)
    assert element


@when("user navigates Pro Packlink")
def step_impl(context):
    page = Page(context)
    page.find_element_waiting(base_page.navigate_to_pro).click()


@when("user clicks on Register button")
def step_impl(context):
    print('I click register')
    page = Page(context)
    page.waiting(page.find_element_by_locator(register_page.register_button)).click()
    assert page.browser.current_url.endswith(register_page.url)  # Check that we navigated to the correct address


@then("user sees the registration form with five fields")
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


@given("internet user is on register page")
def step_impl(context):
    page = Page(context)
    page.goto_register_page()


@when("user registers with {email} and password")
def step_impl(context, email):
    page = RegisterPage(context)
    password = random_password(10)
    context.first_time_password = password
    context.first_time_email = email
    page.register_user(email, password=None)
    # TODO add something to wait for when registration finishes and come back to registration page


@then("user will land into the onboarding process")
def step_impl(context):
    page = Page(context)
    next_button = page.find_element_waiting(onboarding_page.next_button)
    assert next_button
    # assert page.browser.current_url.endswith('onboarding')
    # we have to logout here!

