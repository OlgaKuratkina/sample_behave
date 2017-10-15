from behave import *
from DOM.pages import Page, CreateSendingPage
from DOM.search_page import SearchPage

from DOM.locators import *


@given('a registered client logged in')
def step_impl(context):
    context.execute_steps('Given registered client logged in')


@when('a service has been selected')
def step_impl(context):
    page = SearchPage(context)
    page.choose_create_new_sending()

    destination = page.find_element_by_locator(search_page.postal_code)
    page.send_text_to_validated_field(destination, 'Madrid')
    destination.submit()

    context.execute_steps('Then client with choose the first service in the list')

    header = page.find_element_waiting(create_sending_page.header)
    assert header


@then('he will save the shipment as a draft')
def step_impl(context):
    page = Page(context)
    save_button = page.find_element_by_locator(create_sending_page.save_button)
    save_button.click()


@then('it will appear in the shipment list')
def step_impl(context):
    page = CreateSendingPage(context)
    sendings_table = page.find_element_waiting(create_sending_page.sendings_table, many=True)
    assert len(sendings_table) > 1  # assuming one row is always empty


@given('a registered client')
def step_impl(context):
    pass

# Could be Implemented for deleting the shipment


@when('on the shipments page')
def step_impl(context):
    page = Page(context)
    page.goto_shipments_page()


@then('he can delete shipment')
def step_impl(context):
    page = Page(context)
    sending = page.find_element_waiting(create_sending_page.sending_link, many=True)
    sending[0].click()

    delete_button = page.find_element_waiting(create_sending_page.delete_button)
    delete_button.click()


@then('it will disappear from the list')
def step_impl(context):
    page = Page(context)
    sendings_table = page.find_element_waiting(create_sending_page.sendings_table, many=True)
    assert len(sendings_table) == 1  # assuming one row is always empty