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
    group_testing_double_click()
    FlutterReportGenerator.generate_report()


def group_testing_double_click():
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
    double_click("GestureDetectorTest")
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is GestureDetectorDoubleClick"))


def testing_gesture_detector_key(_):
    reset()
    double_click("gesture-detector", how_to_click=HowToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is GestureDetectorDoubleClick"))


def testing_gesture_detector_text(_):
    reset()
    double_click("GestureDetector", how_to_click=HowToClick.BY_TEXT)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is GestureDetectorDoubleClick"))


def testing_gesture_detector_type(_):
    reset()
    # Less critical bug so ignored
    double_click("GestureDetector", how_to_click=HowToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is GestureDetectorDoubleClick"))


def testing_gesture_detector(_):
    reset()
    double_click("GestureDetector", how_to_click=HowToClick.GESTURE_DETECTOR)
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is GestureDetectorDoubleClick"))


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
    double_click("InkWell", )
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is InkWellDoubleClick"))


def testing_ink_well_id(_):
    reset()
    double_click("ink-well", how_to_click=HowToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellDoubleClick"))


def testing_ink_well_text(_):
    reset()
    double_click("InkWell", how_to_click=HowToClick.BY_TEXT)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellDoubleClick"))


def testing_ink_well_type(_):
    reset()
    # Less critical bug, so ignored
    double_click("InkWell", how_to_click=HowToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellDoubleClick"))


def testing_ink_well(_):
    reset()
    double_click("InkWell", how_to_click=HowToClick.INKWELL)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellDoubleClick"))


def reset():
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("reset")).click()
    finds_reset_output()


def finds_reset_output():
    assert finds_some_widgets(UtilsSetup.finder.by_text("No Output"))


if __name__ == "__main__":
    main()
