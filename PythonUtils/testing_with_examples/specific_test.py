from utils import *
from testing_with_examples.driver import *
from appium import webdriver
from appium_flutter_finder import FlutterFinder, FlutterElement
import traceback
from time import sleep


def main():
    driver = webdriver.Remote(appium_server_url, capabilities)
    UtilsSetup.setup(driver, FlutterFinder())
    click("Click Test Screen", what_to_click=WhatToClick.ELEVATED_BUTTON)
    click("GestureDetectorChild", what_to_click=WhatToClick.BY_SEMANTIC_LABEL)
    sleep(1)



if __name__ == "__main__":
    main()
