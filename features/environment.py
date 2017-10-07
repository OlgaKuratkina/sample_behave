from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os
import datetime


def before_all(context):
    print("Executing before all")
    context.now = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    context.browser = webdriver.Firefox()
    # context.browser = webdriver.Firefox(firefox_binary=FirefoxBinary("c:\\Program Files\\Mozilla Firefox\\firefox.exe"))
    context.browser.set_window_size(1280, 800)


def before_feature(context, feature):
    print(feature.tags)


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
    context.browser.quit()