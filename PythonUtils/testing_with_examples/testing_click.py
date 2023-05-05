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
    group_testing_click()
    FlutterReportGenerator.generate_report()


def group_testing_click():
    test(
        "Initial Setup",
        init,
    )
    group(
        "Testing Elevated Button",
        group_elevated_button
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
    group(
        "Testing Icon Button",
        group_icon_button
    )
    group(
        "Testing Floating Action Button",
        group_floating_action
    )
    group(
        "Testing Hard Coded",
        group_hard_core,
    )


def init(_):
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("/ClickTestScreen")).click()
    UtilsSetup.driver.execute_script('flutter:waitFor', UtilsSetup.finder.by_type("ClickTestScreen"), 1500)
    finds_reset_output()


def group_elevated_button():
    test(
        "Testing Elevated semantic",
        testing_elevated_semantic,
    )
    test(
        "Testing Elevated Key",
        testing_elevated_key,
    )
    test(
        "Testing Elevated Text",
        testing_elevated_text,
    )
    test(
        "Testing Elevated Type",
        testing_elevated_type,
    )
    test(
        "Testing Elevated",
        testing_elevated,
    )


def testing_elevated_semantic(_):
    reset()
    click("ElevatedButton", )
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is ElevatedButton")), "HowToClick.BY_SEMANTIC_LABEL"


def testing_elevated_key(_):
    reset()
    click("elevated-button", how_to_click=HowToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is ElevatedButton")), "HowToClick.BY_VALUE_KEY"


def testing_elevated_text(_):
    reset()
    click("ElevatedButton", how_to_click=HowToClick.BY_TEXT)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is ElevatedButton")), "HowToClick.BY_TEXT"


def testing_elevated_type(_):
    reset()
    click("ElevatedButton", how_to_click=HowToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is ElevatedButton")), "HowToClick.BY_TYPE"


def testing_elevated(_):
    reset()
    click("ElevatedButton", how_to_click=HowToClick.ELEVATED_BUTTON)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is ElevatedButton")), "HowToClick.ELEVATED_BUTTON "


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
    click("GestureDetectorTest")
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_SEMANTIC_LABEL Child"


def testing_gesture_detector_key(_):
    reset()
    click("gesture-detector", how_to_click=HowToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_VALUE_KEY"


def testing_gesture_detector_text(_):
    reset()
    click("GestureDetector", how_to_click=HowToClick.BY_TEXT)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_TEXT"


def testing_gesture_detector_type(_):
    reset()
    # Less critical bug so ignored
    click("GestureDetector", how_to_click=HowToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is GestureDetectorClick")), "HowToClick.BY_TYPE"


def testing_gesture_detector(_):
    reset()
    click("GestureDetector", how_to_click=HowToClick.GESTURE_DETECTOR)
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is GestureDetectorClick")), "HowToClick.GESTURE_DETECTOR"


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
    click("InkWell", )
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is InkWellClick")), "HowToClick.BY_SEMANTIC_LABEL"


def testing_ink_well_id(_):
    reset()
    click("ink-well", how_to_click=HowToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellClick")), "HowToClick.BY_VALUE_KEY"


def testing_ink_well_text(_):
    reset()
    click("InkWell", how_to_click=HowToClick.BY_TEXT)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellClick")), "HowToClick.BY_TEXT"


def testing_ink_well_type(_):
    reset()
    # Less critical bug, so ignored
    click("InkWell", how_to_click=HowToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellClick")), "HowToClick.BY_TYPE"


def testing_ink_well(_):
    reset()
    click("InkWell", how_to_click=HowToClick.INKWELL)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is InkWellClick")), "HowToClick.INKWELL"


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
    click("TextButton")
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is TextButtonClick")), "HowToClick.BY_SEMANTIC_LABEL"


def testing_text_button_id(_):
    reset()
    click("text-button", how_to_click=HowToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is TextButtonClick")), "HowToClick.BY_VALUE_KEY"


def testing_text_button_text(_):
    reset()
    click("TextButton", how_to_click=HowToClick.BY_TEXT)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is TextButtonClick")), "HowToClick.BY_TEXT"


def testing_text_button_type(_):
    reset()
    click("TextButton", how_to_click=HowToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is TextButtonClick")), "HowToClick.BY_TYPE"


def testing_text_button(_):
    reset()
    click("TextButton", how_to_click=HowToClick.TEXT_BUTTON)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is TextButtonClick")), "HowToClick.TEXT_BUTTON"


def group_icon_button():
    test(
        "Testing Icon Button Semantic",
        testing_icon_button_semantic,
    )
    test(
        "Testing Icon Button Id",
        testing_icon_button_id,
    )
    test(
        "Testing Icon Button Type",
        testing_icon_button_type,
    )


def testing_icon_button_semantic(_):
    # Needs to do some setup in Semantic Widget: explicitChildNodes: true
    # View this issue :https://github.com/flutter/flutter/issues/126059
    reset()
    click("IconButton", )
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is IconButton")), "HowToClick.BY_SEMANTIC_LABEL"


def testing_icon_button_id(_):
    reset()
    click("icon-button", how_to_click=HowToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is IconButton")), "HowToClick.BY_VALUE_KEY"


def testing_icon_button_type(_):
    # Less critical bug, so ignroed
    reset()
    click("IconButton", how_to_click=HowToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is IconButton")), "HowToClick.BY_TYPE"


def group_floating_action():
    test(
        "Testing Floating Semantic",
        testing_floating_semantic,
    )
    test(
        "Testing Floating Id",
        testing_floating_id,
    )
    test(
        "Testing Floating Type",
        testing_floating_type,
    )
    test(
        "Testing Floating",
        testing_floating,
    )


def testing_floating_semantic(_):
    reset()
    click("FloatingActionButton", )
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is FloatingActionButton")), "HowToClick.BY_SEMANTIC_LABEL"


def testing_floating_id(_):
    reset()
    click("floating-action-button", how_to_click=HowToClick.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is FloatingActionButton")), "HowToClick.BY_VALUE_KEY"


def testing_floating_type(_):
    reset()
    click("FloatingActionButton", how_to_click=HowToClick.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is FloatingActionButton")), "HowToClick.BY_TYPE"


def testing_floating(_):
    reset()
    click("FloatingActionButton", how_to_click=HowToClick.FLOATING_ACTION_BUTTON)
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is FloatingActionButton")), "HowToClick.FLOATING_ACTION_BUTTON"


def group_hard_core():
    test(
        "Testing Simple Ancestor",
        testing_simple_ancestor,
    )
    test(
        "Testing Complex Ancestor",
        testing_complex_ancestor,
    )
    test(
        "Testing Simple Descendant",
        testing_simple_descendant,
    )
    test(
        "Testing Complex Descendant",
        testing_complex_descendant,
    )


def testing_simple_ancestor(_):
    reset()
    click(UtilsSetup.finder.by_ancestor(
        UtilsSetup.finder.by_text("ElevatedButton"),
        UtilsSetup.finder.by_type("ElevatedButton"),
    ), how_to_click=HowToClick.HARD_CODED)
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is ElevatedButton")), "HowToClick.BY_SEMANTIC_LABEL"


def testing_complex_ancestor(_):
    reset()
    click(UtilsSetup.finder.by_ancestor(
        UtilsSetup.finder.by_semantics_label("ElevatedButtonChild"),
        UtilsSetup.finder.by_type("ElevatedButton"),
    ), how_to_click=HowToClick.HARD_CODED)
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is ElevatedButton")), "HowToClick.BY_SEMANTIC_LABEL"


def testing_simple_descendant(_):
    reset()
    click(
        UtilsSetup.finder.by_descendant(
            UtilsSetup.finder.by_type("ElevatedButton"),
            UtilsSetup.finder.by_text("ElevatedButton")
        ),
        how_to_click=HowToClick.HARD_CODED,
    )
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is ElevatedButton")), "HowToClick.BY_SEMANTIC_LABEL"


def testing_complex_descendant(_):
    reset()
    click(
        UtilsSetup.finder.by_descendant(
            UtilsSetup.finder.by_type("Column"),
            UtilsSetup.finder.by_type("ElevatedButton")
        ),
        how_to_click=HowToClick.HARD_CODED,
    )
    assert finds_some_widgets(
        UtilsSetup.finder.by_text("Output is ElevatedButton")), "HowToClick.BY_SEMANTIC_LABEL"


def reset():
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("reset")).click()
    finds_reset_output()


def finds_reset_output():
    assert finds_some_widgets(UtilsSetup.finder.by_text("No Output")), "Finds No Output"


if __name__ == "__main__":
    main()
