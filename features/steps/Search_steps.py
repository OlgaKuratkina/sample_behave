from behave import *
from features.utils.pages import Page, RegisterPage
from features.utils.locators import *
from features.utils.helper_methods import random_password, random_phone


# @given('registered user')
# def step_impl(context):
#     pass
#
#
# @when("user log in for the first time")
# def step_impl(context):
#     context.execute_steps("user navigates Pro Packlink")
#     page = Page(context)
#     page.find_element_by_locator(register_page.login_button).click()
#
#
# @then("user will complete the onboarding process")
# def step_impl(context):
#     pass