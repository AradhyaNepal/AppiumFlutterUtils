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
    # testing_click_on_elevated_button(driver, finder) #PASS
    #testing_click_on_gesture_detector(driver, finder)
    testing_click_on_ink_well(driver, finder)
    # testing_click_on_text_button(driver, finder) #PASS
    # testing_click_on_icon_button(driver, finder)
    # testing_click_on_floating_action(driver, finder) #PASS





def init(driver, finder):
    try:
        FlutterElement(driver, finder.by_value_key("/ClickTestScreen")).click()
        assert finds_some_widgets(finder.by_type("ClickTestScreen")), "Finds ClickTestScreen"
        finds_reset_output(finder)
    except Exception as e:
        print("Setting up click setup Failed")
        print(e)
        print(traceback.format_exc())


def testing_click_on_elevated_button(driver, finder):
    try:
        click("ElevatedButtonParent", how_to_click=HowToClick.BY_SEMANTIC_LABEL)
        assert finds_some_widgets(finder.by_text("Output is ElevatedButton")), "HowToClick.BY_SEMANTIC_LABEL Parent"
        reset(driver, finder)
        # click("ElevatedButtonChild", how_to_click=HowToClick.BY_SEMANTIC_LABEL, identifier_added_to_child=True)
        # assert finds_some_widgets(finder.by_text("Output is ElevatedButton")), "HowToClick.BY_SEMANTIC_LABEL Child"
        # reset(driver, finder)
        click("elevated-button", how_to_click=HowToClick.BY_VALUE_KEY)
        assert finds_some_widgets(finder.by_text("Output is ElevatedButton")), "HowToClick.BY_VALUE_KEY"
        reset(driver, finder)
        click("ElevatedButton", how_to_click=HowToClick.BY_TEXT)
        assert finds_some_widgets(finder.by_text("Output is ElevatedButton")), "HowToClick.BY_TEXT"
        reset(driver, finder)
        click("ElevatedButton", how_to_click=HowToClick.BY_TYPE)
        assert finds_some_widgets(finder.by_text("Output is ElevatedButton")), "HowToClick.BY_TYPE"
        reset(driver, finder)
        click("ElevatedButton", how_to_click=HowToClick.ELEVATED_BUTTON)
        assert finds_some_widgets(finder.by_text("Output is ElevatedButton")), "HowToClick.ELEVATED_BUTTON "
        reset(driver, finder)
    except Exception as e:
        print("Testing Click On Elevated Button Failed")
        print(e)
        print(traceback.format_exc())


def testing_click_on_gesture_detector(driver, finder):
    try:
        click("GestureDetectorParent", how_to_click=HowToClick.BY_SEMANTIC_LABEL)
        assert finds_some_widgets(
            finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_SEMANTIC_LABEL Parent"
        reset(driver, finder)
        # click("GestureDetectorChild", how_to_click=HowToClick.BY_SEMANTIC_LABEL, identifier_added_to_child=True)
        # assert finds_some_widgets(
        #     finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_SEMANTIC_LABEL Child"
        # reset(driver, finder)
        click("gesture-detector", how_to_click=HowToClick.BY_VALUE_KEY)
        assert finds_some_widgets(finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_VALUE_KEY"
        reset(driver, finder)
        click("GestureDetector", how_to_click=HowToClick.BY_TEXT)
        assert finds_some_widgets(finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_TEXT"
        reset(driver, finder)
        click("GestureDetector", how_to_click=HowToClick.BY_TYPE)
        assert finds_some_widgets(finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_TYPE"
        reset(driver, finder)
        click("GestureDetector", how_to_click=HowToClick.GESTURE_DETECTOR)
        assert finds_some_widgets(finder.by_text("Output is GestureDetectorClick")), "HowToClick.GESTURE_DETECTOR"
        reset(driver, finder)
    except Exception as e:
        print("Testing Click On GestureDetectorClick Failed")
        print(e)
        print(traceback.format_exc())


def testing_click_on_ink_well(driver, finder):
    try:
        click("InkWellParent", how_to_click=HowToClick.BY_SEMANTIC_LABEL)
        assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.BY_SEMANTIC_LABEL Parent"
        reset(driver, finder)
        # click("InkWellChild", how_to_click=HowToClick.BY_SEMANTIC_LABEL, identifier_added_to_child=True)
        # assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.BY_SEMANTIC_LABEL Child"
        # reset(driver, finder)
        click("ink-well", how_to_click=HowToClick.BY_VALUE_KEY)
        assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.BY_VALUE_KEY"
        reset(driver, finder)
        click("InkWell", how_to_click=HowToClick.BY_TEXT)
        assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.BY_TEXT"
        reset(driver, finder)
        click("InkWell", how_to_click=HowToClick.BY_TYPE)
        assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.BY_TYPE"
        reset(driver, finder)
        click("InkWell", how_to_click=HowToClick.INKWELL)
        assert finds_some_widgets(finder.by_text("Output is InkWellClick")), "HowToClick.INKWELL"
        reset(driver, finder)
    except Exception as e:
        print("Testing Click On InkWellClick Failed")
        print(e)
        print(traceback.format_exc())


def testing_click_on_text_button(driver, finder):
    try:
        click("TextButtonParent", how_to_click=HowToClick.BY_SEMANTIC_LABEL)
        assert finds_some_widgets(finder.by_text("Output is TextButtonClick")), "HowToClick.BY_SEMANTIC_LABEL Parent"
        reset(driver, finder)
        # click("TextButtonChild", how_to_click=HowToClick.BY_SEMANTIC_LABEL, identifier_added_to_child=True)
        # assert finds_some_widgets(finder.by_text("Output is TextButtonClick")), "HowToClick.BY_SEMANTIC_LABEL Child"
        # reset(driver, finder)
        click("text-button", how_to_click=HowToClick.BY_VALUE_KEY)
        assert finds_some_widgets(finder.by_text("Output is TextButtonClick")), "HowToClick.BY_VALUE_KEY"
        reset(driver, finder)
        click("TextButton", how_to_click=HowToClick.BY_TEXT)
        assert finds_some_widgets(finder.by_text("Output is TextButtonClick")), "HowToClick.BY_TEXT"
        reset(driver, finder)
        click("TextButton", how_to_click=HowToClick.BY_TYPE)
        assert finds_some_widgets(finder.by_text("Output is TextButtonClick")), "HowToClick.BY_TYPE"
        reset(driver, finder)
        click("TextButton", how_to_click=HowToClick.TEXT_BUTTON)
        assert finds_some_widgets(finder.by_text("Output is TextButtonClick")), "HowToClick.TEXT_BUTTON"
        reset(driver, finder)
    except Exception as e:
        print("Testing Click On TextButtonClick Failed")
        print(e)
        print(traceback.format_exc())


def testing_click_on_icon_button(driver, finder):
    try:
        click("IconButtonParent", how_to_click=HowToClick.BY_SEMANTIC_LABEL)
        assert finds_some_widgets(finder.by_text("Output is IconButton")), "HowToClick.BY_SEMANTIC_LABEL Parent"
        reset(driver, finder)
        # click("IconButtonChild", how_to_click=HowToClick.BY_SEMANTIC_LABEL, identifier_added_to_child=True)
        # assert finds_some_widgets(finder.by_text("Output is IconButton")), "HowToClick.BY_SEMANTIC_LABEL Child"
        # reset(driver, finder)
        click("icon-button", how_to_click=HowToClick.BY_VALUE_KEY)
        assert finds_some_widgets(finder.by_text("Output is IconButton")), "HowToClick.BY_VALUE_KEY"
        reset(driver, finder)
        click("IconButton", how_to_click=HowToClick.BY_TYPE)
        assert finds_some_widgets(finder.by_text("Output is IconButton")), "HowToClick.BY_TYPE"
        reset(driver, finder)
        # click("IconButton", how_to_click=HowToClick.ICON_BUTTON)
        # assert finds_some_widgets(finder.by_text("Output is IconButton")), "HowToClick.ICON_BUTTON"
        # reset(driver, finder)
    except Exception as e:
        print("Testing Click On IconButton Failed")
        print(e)
        print(traceback.format_exc())


def testing_click_on_floating_action(driver, finder):
    try:
        click("FloatingActionButtonParent", how_to_click=HowToClick.BY_SEMANTIC_LABEL)
        assert finds_some_widgets(
            finder.by_text("Output is FloatingActionButton")), "HowToClick.BY_SEMANTIC_LABEL Parent"
        reset(driver, finder)
        # click("FloatingActionButtonChild", how_to_click=HowToClick.BY_SEMANTIC_LABEL, identifier_added_to_child=True)
        # assert finds_some_widgets(
        #     finder.by_text("Output is FloatingActionButton")), "HowToClick.BY_SEMANTIC_LABEL Child"
        # reset(driver, finder)
        click("floating-action-button", how_to_click=HowToClick.BY_VALUE_KEY)
        assert finds_some_widgets(finder.by_text("Output is FloatingActionButton")), "HowToClick.BY_VALUE_KEY"
        reset(driver, finder)
        click("FloatingActionButton", how_to_click=HowToClick.BY_TYPE)
        assert finds_some_widgets(finder.by_text("Output is FloatingActionButton")), "HowToClick.BY_TYPE"
        reset(driver, finder)
        click("FloatingActionButton", how_to_click=HowToClick.FLOATING_ACTION_BUTTON)
        assert finds_some_widgets(finder.by_text("Output is FloatingActionButton")), "HowToClick.FLOATING_ACTION_BUTTON"
        reset(driver, finder)
    except Exception as e:
        print("Testing Click On FloatingActionButton Failed")
        print(e)
        print(traceback.format_exc())


def reset(driver, finder):
    FlutterElement(driver, finder.by_value_key("reset")).click()
    finds_reset_output(finder)


def finds_reset_output(finder):
    assert finds_some_widgets(finder.by_text("No Output")), "Finds No Output"


if __name__ == "__main__":
    main()
