from utils import *
from testing_with_examples.driver import *
from appium import webdriver
from appium_flutter_finder import FlutterFinder, FlutterElement
import traceback


def main():
    driver = webdriver.Remote(appium_server_url, capabilities)
    finder = FlutterFinder()
    UtilsSetup.setup(driver, finder)
    init(driver, finder)
    testing_click_on_gesture_detector(driver, finder)
    testing_click_on_ink_well(driver, finder)


def init(driver, finder):
    try:
        FlutterElement(driver, finder.by_value_key("/ClickTestScreen")).click()
        assert finds_some_widgets(finder.by_type("ClickTestScreen")), "Finds ClickTestScreen"
        finds_reset_output(finder)
    except Exception as e:
        print("Setting up click setup Failed")
        print(e)
        print(traceback.format_exc())


def testing_click_on_gesture_detector(driver, finder):
    try:
        double_click("GestureDetectorParent", how_to_click=HowToClick.BY_SEMANTIC_LABEL)
        assert finds_some_widgets(
            finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_SEMANTIC_LABEL Parent"
        reset(driver, finder)
        # double_click("GestureDetectorChild", how_to_click=HowToClick.BY_SEMANTIC_LABEL, identifier_added_to_child=True)
        # assert finds_some_widgets(
        #     finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_SEMANTIC_LABEL Child"
        # reset(driver, finder)
        double_click("gesture-detector", how_to_click=HowToClick.BY_VALUE_KEY)
        assert finds_some_widgets(finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_VALUE_KEY"
        reset(driver, finder)
        double_click("GestureDetector", how_to_click=HowToClick.BY_TEXT)
        assert finds_some_widgets(finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_TEXT"
        reset(driver, finder)
        double_click("GestureDetector", how_to_click=HowToClick.BY_TYPE)
        assert finds_some_widgets(finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_TYPE"
        reset(driver, finder)
        double_click("GestureDetector", how_to_click=HowToClick.GESTURE_DETECTOR)
        assert finds_some_widgets(finder.by_text("Output is GestureDetectorClick")), "HowToClick.GESTURE_DETECTOR"
        reset(driver, finder)
    except Exception as e:
        print("Testing Click On GestureDetectorClick Failed")
        print(e)
        print(traceback.format_exc())


def testing_click_on_ink_well(driver, finder):
    try:
        double_click("InkWellParent", how_to_click=HowToClick.BY_SEMANTIC_LABEL)
        assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.BY_SEMANTIC_LABEL Parent"
        reset(driver, finder)
        # double_click("InkWellChild", how_to_click=HowToClick.BY_SEMANTIC_LABEL, identifier_added_to_child=True)
        # assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.BY_SEMANTIC_LABEL Child"
        # reset(driver, finder)
        double_click("ink-well", how_to_click=HowToClick.BY_VALUE_KEY)
        assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.BY_VALUE_KEY"
        reset(driver, finder)
        double_click("InkWell", how_to_click=HowToClick.BY_TEXT)
        assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.BY_TEXT"
        reset(driver, finder)
        double_click("InkWell", how_to_click=HowToClick.BY_TYPE)
        assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.BY_TYPE"
        reset(driver, finder)
        double_click("InkWell", how_to_click=HowToClick.INKWELL)
        assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.INKWELL"
        reset(driver, finder)
    except Exception as e:
        print("Testing Click On InkWellClick Failed")
        print(e)
        print(traceback.format_exc())


def reset(driver, finder):
    FlutterElement(driver, finder.by_value_key("reset")).click()
    finds_reset_output(finder)


def finds_reset_output(finder):
    assert finds_some_widgets(finder.by_text("No Output")), "Finds No Output"


if __name__ == "__main__":
    main()
