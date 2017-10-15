from behave import *
from DOM.search_page import SearchPage
from DOM.register_page import RegisterPage
from DOM.onboarding_page import OnboardingPage

from DOM.locators import *


@given('registered user')
def step_impl(context):
    page = OnboardingPage(context)
    page.goto_base_page()
    # page.safe_logout()


@when("user log in for the first time")
def step_impl(context):
    page = RegisterPage(context)
    page.goto_pro_page()

    email = context.first_time_email
    password = context.first_time_password
    page.find_element_by_locator(register_page.login_button).click()
    page.login_user(email=email, password=password)


@then("user will complete the onboarding process")
def step_impl(context):
    page = OnboardingPage(context)

    page.scroll_down()
    next_button = page.find_element_waiting(onboarding_page.next_button)
    next_button.click()
    page.fill_in_onboarding_data()  #TODO uncomment when its ready
    page.fill_in_package_info()
    create_link = page.find_element_waiting(onboarding_form.create_link)
    assert create_link
    page.safe_logout()


@given('registered client logged in')
def step_impl(context):
    username = context.username
    password = context.password
    # context.execute_steps("Given internet user is on start page")
    # context.execute_steps("When user navigates Pro Packlink")

    page = RegisterPage(context)
    page.goto_pro_page()
    page.find_element_by_locator(register_page.login_button).click()
    page.login_user(username, password)


@when('performing a search with set of details')
def step_impl(context):
    for row in context.table:
        address, destination, weight, length, width, height = row

        page = SearchPage(context)

        page.choose_create_new_sending()

        # page.delete_predefined_address()
        page.search_for_sending(address, destination, weight, length, width, height)
        services = page.find_element_waiting(search_page.service_list, many=True)
        assert len(services) > 0


@then('client with choose the first service in the list')
def step_impl(context):
    page = SearchPage(context)
    services = page.find_element_waiting(search_page.services_list_buttons, many=True)
    services[0].click()

    details = page.find_element_waiting(search_page.sending_details)
    print(details.text)
    assert details
