from behave import *
from DOM.pages import Page
from DOM.register_page import RegisterPage
from DOM.onboarding_page import OnboardingPage

from DOM.locators import *


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
    page.waiting(page.find_element_by_locator(register_page.register_button)).click()
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


@given("internet user is on register page")
def step_impl(context):
    page = Page(context)
    page.goto_register_page()


@when("user registers with {email} and {password}")
def step_impl(context, email, password):
    page = RegisterPage(context)
    page.register_user(email, password)
    # TODO add something to wait for when registration finishes and come back to registration page


@then("user will land into the onboarding process")
def step_impl(context):
    page = Page(context)
    next_button = page.find_element_waiting(onboarding_page.next_button)
    assert not next_button
    pass


@given('registered user')
def step_impl(context):
    page = OnboardingPage(context)
    page.goto_base_page()
    page.safe_logout()


@when("user log in for the first time with {email} and {password}")
def step_impl(context, email, password):
    context.execute_steps("Given internet user is on start page")
    context.execute_steps("When user navigates Pro Packlink")

    page = RegisterPage(context)
    page.find_element_by_locator(register_page.login_button).click()
    page.login_user(email=email, password=password)


@then("user will complete the onboarding process")
def step_impl(context):
    page = OnboardingPage(context)

    page.scroll_down()
    next_button = page.find_element_waiting(onboarding_page.next_button)
    next_button.click()
    # page.fill_in_onboarding_data()  #TODO uncomment when its ready
    # page.fill_in_package_info()
    # create_link = page.find_element_waiting(onboarding_form.create_link)
    # assert create_link
    page.safe_logout()

