from utils import *
from testing_with_examples.driver import *
from appium import webdriver
from appium_flutter_finder import FlutterFinder, FlutterElement
import traceback
from time import sleep


def main():
    driver = webdriver.Remote(appium_server_url, capabilities)
    UtilsSetup.setup(driver, FlutterFinder())
    click("Click Test Screen",how_to_click=HowToClick.ELEVATED_BUTTON)
    # click("GestureDetector",how_to_click=HowToClick.GESTURE_DETECTOR)
    # sleep(1)
    # click("InkWell",how_to_click=HowToClick.INKWELL)
    # sleep(1)
    # click("",how_to_click=HowToClick.FLOATING_ACTION_BUTTON)
    # sleep(1)
    # click("TextButton",how_to_click=HowToClick.TEXT_BUTTON)
    # sleep(1)
    # click("elevated-button",how_to_click=HowToClick.BY_VALUE_KEY)
    # sleep(1)
    # click("FloatingActionButton",how_to_click=HowToClick.BY_TYPE)
    # sleep(1)
    # click("InkWell",how_to_click=HowToClick.BY_TEXT)
    # sleep(1)
    # click("TextButtonParent",how_to_click=HowToClick.BY_SEMANTIC_LABEL)
    # sleep(1)
    click("Divider",how_to_click=HowToClick.BY_TYPE)
    sleep(1)
    # click("TextButton",how_to_click=HowToClick.ICON_BUTTON) Todo


if __name__ == "__main__":
    main()
