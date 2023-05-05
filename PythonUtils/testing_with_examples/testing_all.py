from utils import *
from testing_with_examples.driver import *
from appium import webdriver
from appium_flutter_finder import FlutterFinder, FlutterElement
import traceback
from appium_flutter_report import *
from testing_click import group_testing_click
from testing_double_click import group_testing_double_click
from testing_long_click import group_testing_long_click
from  testing_wait import group_testing_wait


def main():
    driver = webdriver.Remote(appium_server_url, capabilities)
    finder = FlutterFinder()
    UtilsSetup.setup(driver, finder)
    FlutterReportGenerator.setup(driver, "Python Utils", "./output/", capabilities)
    group(
        "Testing Click",
        group_testing_click,
    )
    __go_back()
    group(
        "Testing Double Click",
        group_testing_double_click,
    )
    __go_back()
    group(
        "Testing Long Click",
        group_testing_long_click,
    )
    group(
        "Testing Wait",
        group_testing_wait,
    )
    FlutterReportGenerator.generate_report()


def __go_back():
    UtilsSetup.driver.switch_to.context("NATIVE_APP")
    UtilsSetup.driver.back()
    UtilsSetup.driver.switch_to.context("FLUTTER")


if __name__ == "__main__":
    main()
