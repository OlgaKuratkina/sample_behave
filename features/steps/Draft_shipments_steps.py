from behave import *
from DOM.pages import CreateSendingPage

from DOM.locators import *


@given('a registered client')
def step_impl(context):
    context.execute_steps('Given registered user')
    context.execute_steps('Given registered client logged in')


@when('a service has been selected')
def step_impl(context):
    context.execute_steps('When performing a search with set of details')
    context.execute_steps('Then client with choose the first service in the list')
    page = CreateSendingPage(context)
    header = page.get_attribute_safe(create_sending_page.header, 'text')
    assert 'Creando envío' in header


@then('he will save the shipment as a draft')
def step_impl(context):
    page = CreateSendingPage(context)
    save_button = page.find_element_by_locator(create_sending_page.save_button)
    save_button.click()


@then('it will appear in the shipment list')
def step_impl(context):
    pass