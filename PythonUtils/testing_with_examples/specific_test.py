from utils import *
from testing_with_examples.driver import *
from appium import webdriver
from appium_flutter_finder import FlutterFinder, FlutterElement
import traceback
from time import sleep


def main():
    driver = webdriver.Remote(appium_server_url, capabilities)
    UtilsSetup.setup(driver, FlutterFinder())
    click("Click Test Screen", how_to_click=HowToClick.ELEVATED_BUTTON_TEXT)
    click("GestureDetectorChild", how_to_click=HowToClick.BY_SEMANTIC_LABEL)
    sleep(1)



if __name__ == "__main__":
    main()
