from utils import *
from testing_with_examples.driver import *
from appium import webdriver
from appium_flutter_finder import FlutterFinder, FlutterElement
import traceback


def main():
    driver = webdriver.Remote(appium_server_url, capabilities)
    finder = FlutterFinder()
    initial_setup(driver, finder)

    # Testing starts From below
    testing_click_on_elevated_button(driver, finder)


def initial_setup(driver, finder):
    try:
        FlutterElement(driver, finder.by_value_key("/ClickTestScreen")).click()
        assert finds_one_widget(finder.by_type("ClickTestScreen")), "Finds ClickTestScreen"
        finds_reset_output(finder)
    except Exception as e:
        print("Setting up click setup Failed")
        print(e)
        print(traceback.format_exc())


def testing_click_on_elevated_button(driver, finder):
    try:
        click("ElevatedButtonParent", how_to_click=HowToClick.BY_SEMANTIC_LABEL)
        assert finds_one_widget(finder.by_text("Output is ElevatedButton")), "HowToClick.BY_SEMANTIC_LABEL Parent"
        reset(driver, finder)
        click("ElevatedButtonChild", how_to_click=HowToClick.BY_SEMANTIC_LABEL, identifier_added_to_child=True)
        assert finds_one_widget(finder.by_text("Output is ElevatedButton")), "HowToClick.BY_SEMANTIC_LABEL Child"
        reset(driver, finder)
        click("elevated-button", how_to_click=HowToClick.BY_VALUE_KEY)
        assert finds_one_widget(finder.by_text("Output is ElevatedButton")), "HowToClick.BY_VALUE_KEY Child"
        reset(driver, finder)
        click("ElevatedButton", how_to_click=HowToClick.BY_TEXT)
        assert finds_one_widget(finder.by_text("Output is ElevatedButton")), "HowToClick.BY_TEXT Child"
        reset(driver, finder)
        click("ElevatedButton", how_to_click=HowToClick.BY_TYPE)
        assert finds_one_widget(finder.by_text("Output is ElevatedButton")), "HowToClick.BY_TYPE Child"
        reset(driver, finder)
        click("ElevatedButton", how_to_click=HowToClick.ELEVATED_BUTTON)
        assert finds_one_widget(finder.by_text("Output is ElevatedButton")), "HowToClick.ELEVATED_BUTTON Child"
        reset(driver, finder)
    except Exception as e:
        print("Testing Click On Elevated Button Failed")
        print(e)
        print(traceback.format_exc())


def reset(driver, finder):
    FlutterElement(driver, finder.by_value_key("reset")).click()
    finds_reset_output(finder)


def finds_reset_output(finder):
    assert finds_one_widget(finder.by_text("No Output")), "Finds No Output"


def finds_one_widget(finder: FlutterFinder) -> bool:
    try:
        self.driver.execute_script('flutter:waitFor', finder, 1000)
        return True
    except Exception as e:
        return False


if __name__ == "__main__":
    main()
