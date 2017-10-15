from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def before_all(context):
    print("Executing before all")
    context.timeout_tries = 5
    context.logging = logging
    context.username = 'qacandidaeolgak@packlink.es'
    context.password = '145qwerty'

    context.first_time_email = ''
    context.first_time_password = ''
    context.sendings = 0


def before_feature(context, feature):
    context.browser = webdriver.Firefox()
    # context.browser = webdriver.Firefox(firefox_binary=FirefoxBinary("c:\\Program Files\\Mozilla Firefox\\firefox.exe"))
    context.browser.maximize_window()
    context.browser.implicitly_wait(1)


def after_feature(context, feature):
    print('Testing finished')
    context.browser.quit()
