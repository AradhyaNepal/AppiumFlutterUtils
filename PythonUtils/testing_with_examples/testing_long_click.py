from utils import *
from testing_with_examples.driver import *
from appium import webdriver
from appium_flutter_finder import FlutterFinder, FlutterElement
import traceback
from appium_flutter_report import *


def main():
    driver = webdriver.Remote(appium_server_url, capabilities)
    finder = FlutterFinder()
    UtilsSetup.setup(driver, finder)
    FlutterReportGenerator.setup(driver, "Python Utils", "./output/", capabilities)
    group_testing_long_click()
    FlutterReportGenerator.generate_report()


def group_testing_long_click():
    test(
        "Initial Setup",
        init,
    )
    group(
        "Testing Gesture Detector",
        group_gesture_detector,
    )
    group(
        "Testing Ink Well",
        group_ink_well
    )
    group(
        "Testing Text Button",
        group_text_button
    )


def init(_):
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("/ClickTestScreen")).click()
    UtilsSetup.driver.execute_script('flutter:waitFor', UtilsSetup.finder.by_type("ClickTestScreen"), 1500)
    finds_reset_output()


def group_gesture_detector():
    test(
        "Testing Gesture Semantic",
        testing_gesture_detector_semantic,
    )
    test(
        "Testing Gesture Key",
        testing_gesture_detector_key,
    )
    test(
        "Testing Gesture Text",
        testing_gesture_detector_text,
    )
    test(
        "Testing Gesture Type",
        testing_gesture_detector_type,
    )
    test(
        "Testing Gesture",
        testing_gesture_detector
    )


def testing_gesture_detector_semantic(_):
    # Needs to do some setup in Semantic Widget: explicitChildNodes: true
    # View this issue :https://github.com/flutter/flutter/issues/126059
    reset()
    long_click("GestureDetectorTest")
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is GestureDetectorLongClick"))


def testing_gesture_detector_key(_):
    reset()
    long_click("gesture-detector", what_to_click=WhatToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is GestureDetectorLongClick"))


def testing_gesture_detector_text(_):
    reset()
    long_click("GestureDetector", what_to_click=WhatToClick.BY_TEXT)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is GestureDetectorLongClick"))


def testing_gesture_detector_type(_):
    reset()
    # Less critical bug so ignored
    long_click("GestureDetector", what_to_click=WhatToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is GestureDetectorLongClick"))


def testing_gesture_detector(_):
    reset()
    long_click("GestureDetector", what_to_click=WhatToClick.GESTURE_DETECTOR)
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is GestureDetectorLongClick"))


def group_ink_well():
    test(
        "Testing Ink Well Semantic",
        testing_ink_well_semantic,
    )
    test(
        "Testing Ink Well Id",
        testing_ink_well_id,
    )
    test(
        "Testing Ink Well Text",
        testing_ink_well_text,
    )
    test(
        "Testing Ink Well type",
        testing_ink_well_type,
    )
    test(
        "Testing Ink Well",
        testing_ink_well,
    )


def testing_ink_well_semantic(_):
    reset()
    # Needs to do some setup in Semantic Widget: excludeSemantics: true,
    # View this issue :https://github.com/flutter/flutter/issues/126059
    long_click("InkWell", )
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is InkWellLongClick"))


def testing_ink_well_id(_):
    reset()
    long_click("ink-well", what_to_click=WhatToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellLongClick"))


def testing_ink_well_text(_):
    reset()
    long_click("InkWell", what_to_click=WhatToClick.BY_TEXT)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellLongClick"))


def testing_ink_well_type(_):
    reset()
    # Less critical bug, so ignored
    long_click("InkWell", what_to_click=WhatToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellLongClick"))


def testing_ink_well(_):
    reset()
    long_click("InkWell", what_to_click=WhatToClick.INKWELL)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellLongClick"))


def group_text_button():
    test(
        "Testing Text Button Semantic",
        testing_text_button_semantic,
    )
    test(
        "Testing Text Button Id",
        testing_text_button_id,
    )
    test(
        "Testing Text Button Text",
        testing_text_button_text,
    )
    test(
        "Testing text button type",
        testing_text_button_type,
    )
    test(
        "Testing Text Button",
        testing_text_button,
    )


def testing_text_button_semantic(_):
    reset()
    long_click("TextButton")
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is TextButtonLongClick"))


def testing_text_button_id(_):
    reset()
    long_click("text-button", what_to_click=WhatToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is TextButtonLongClick"))


def testing_text_button_text(_):
    reset()
    long_click("TextButton", what_to_click=WhatToClick.BY_TEXT)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is TextButtonLongClick"))


def testing_text_button_type(_):
    reset()
    long_click("TextButton", what_to_click=WhatToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is TextButtonLongClick"))


def testing_text_button(_):
    reset()
    long_click("TextButton", what_to_click=WhatToClick.TEXT_BUTTON)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is TextButtonLongClick"))


def reset():
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("reset")).click()
    finds_reset_output()


def finds_reset_output():
    assert finds_some_widgets(UtilsSetup.finder.by_text("No Output"))


if __name__ == "__main__":
    main()
