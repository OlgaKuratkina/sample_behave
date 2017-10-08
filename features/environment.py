from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import logging

from DOM.pages import Page

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def before_all(context):
    print("Executing before all")
    context.timeout_tries = 5
    context.logging = logging
    context.username = 'qacandidaeolgak@packlink.es'
    context.password = '145qwerty'
    # context.browser = webdriver.Firefox()
    context.browser = webdriver.Firefox(firefox_binary=FirefoxBinary("c:\\Program Files\\Mozilla Firefox\\firefox.exe"))
    context.browser.maximize_window()
    context.browser.implicitly_wait(1)


# def after_scenario(context, scenario):
#     print("\nscenario status: " + scenario.status + ' - for name: ' + scenario.name + '\n')
#     if scenario.status == "failed":
#         folder = "failed_scenarios_screenshots/" + Portal.ENV + "/" + context.now
#         if not os.path.exists(folder):
#             os.makedirs(folder)
#             file_name = scenario.name + "_failed.png"
#             context.browser.save_screenshot(folder + "/" + file_name)
#             print('Screenshoot for fail: ' + scenario.name + " " + os.path.realpath(file_name) + '\n')


def after_all(context):
    print('Testing finished')
    # context.browser.quit()