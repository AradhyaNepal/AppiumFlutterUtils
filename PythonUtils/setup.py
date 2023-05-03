from appium import webdriver
from appium_flutter_finder import FlutterFinder


class UtilsSetup:
    finder: FlutterFinder
    driver: webdriver.Remote

    @staticmethod
    def setup(driver: webdriver.Remote, finder: FlutterFinder):
        UtilsSetup.driver = driver
        UtilsSetup.finder = finder
