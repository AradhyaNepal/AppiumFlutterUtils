from setup import UtilsSetup
from appium_flutter_finder import FlutterFinder, FlutterElement
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from finds_widget import *


class HowToClick:
    ELEVATED_BUTTON_TEXT = 1
    ELEVATED_BUTTON_ITEM = 12
    GESTURE_DETECTOR_TEXT = 2
    GESTURE_DETECTOR_ITEM = 11
    INKWELL_TEXT = 3
    INKWELL_ITEM = 12
    FLOATING_ACTION_BUTTON = 4
    TEXT_BUTTON = 5
    BY_VALUE_KEY = 7
    BY_TYPE = 8
    BY_TEXT = 9
    BY_SEMANTIC_LABEL = 10  # Default and recommended


class __ClickType:
    CLICK = 1
    DOUBLE_CLICK = 2
    LONG_CLICK = 3


def click(value: str, how_to_click: HowToClick = HowToClick.BY_SEMANTIC_LABEL, from_parent_finder: str = None, ):
    __click(value, __ClickType.CLICK, 0, how_to_click, from_parent_finder)


def double_click(value: str, how_to_click: HowToClick = HowToClick.BY_SEMANTIC_LABEL, from_parent_finder: str = None, ):
    if how_to_click == HowToClick.ELEVATED_BUTTON_TEXT or how_to_click == HowToClick.TEXT_BUTTON or how_to_click == HowToClick.FLOATING_ACTION_BUTTON:
        raise "Cannot Double Tap"
    __click(value, __ClickType.DOUBLE_CLICK, 0, how_to_click, from_parent_finder)


def long_click(value: str, how_to_click: HowToClick = HowToClick.BY_SEMANTIC_LABEL, duration: int = 0,
               from_parent_finder: str = None, ):
    if how_to_click == HowToClick.ELEVATED_BUTTON_TEXT or how_to_click == HowToClick.FLOATING_ACTION_BUTTON:
        raise "Cannot Long Tap"
    __click(value, __ClickType.LONG_CLICK, duration, how_to_click, from_parent_finder)


def __click(value: str, click_type: int, duration: int = None,
            how_to_click: HowToClick = HowToClick.BY_SEMANTIC_LABEL, from_parent_finder: str = None, ):
    match how_to_click:
        case HowToClick.ELEVATED_BUTTON_TEXT:
            __click_if_element_found(
                __find_by_text_of_specific_type_of_button_and_from_specific_parent(value, "ElevatedButton",
                                                                                   from_parent_finder),
                duration=duration,
                click_type=click_type,
            )
        case HowToClick.GESTURE_DETECTOR_TEXT:
            __click_if_element_found(
                __find_by_text_of_specific_type_of_button_and_from_specific_parent(value, "GestureDetector",
                                                                                   from_parent_finder),
                duration=duration,
                click_type=click_type,
            )
        case HowToClick.INKWELL_TEXT:
            __click_if_element_found(
                __find_by_text_of_specific_type_of_button_and_from_specific_parent(value, "InkWell",
                                                                                   from_parent_finder),
                duration=duration,
                click_type=click_type,
            )
        case HowToClick.FLOATING_ACTION_BUTTON:
            __click_if_element_found(
                __find_from_specific_parent(
                    UtilsSetup.finder.by_type("FloatingActionButton"),
                    from_parent_finder,
                ),
                duration=duration,
                click_type=click_type,
            )
        case HowToClick.TEXT_BUTTON:
            __click_if_element_found(
                __find_by_text_of_specific_type_of_button_and_from_specific_parent(value, "TextButton",
                                                                                   from_parent_finder),
                duration=duration,
                click_type=click_type,
            )
        case HowToClick.BY_VALUE_KEY:
            __click_if_element_found(
                __find_from_specific_parent(
                    UtilsSetup.finder.by_value_key(value),
                    from_parent_finder,
                ),
                duration=duration,
                click_type=click_type,
            )
        case HowToClick.BY_TYPE:
            __click_if_element_found(
                __find_from_specific_parent(
                    UtilsSetup.finder.by_type(value),
                    from_parent_finder,
                ),
                duration=duration,
                click_type=click_type,
            )
        case HowToClick.BY_TEXT:
            __click_if_element_found(
                __find_from_specific_parent(
                    UtilsSetup.finder.by_text(value),
                    from_parent_finder,
                ),
                duration=duration,
                click_type=click_type,
            )
        case HowToClick.BY_SEMANTIC_LABEL:
            __click_if_element_found(
                __find_from_specific_parent(
                    UtilsSetup.finder.by_semantics_label(value),
                    from_parent_finder,
                ),
                duration=duration,
                click_type=click_type,
            )


def __find_by_text_of_specific_type_of_button_and_from_specific_parent(value: str, type_of_button: str,
                                                                       from_parent_finder: str) -> str:
    return __find_from_specific_parent(
        UtilsSetup.finder.by_descendant(
            UtilsSetup.finder.by_type(type_of_button),
            UtilsSetup.finder.by_text(value),
        ),
        from_parent_finder,
    )


def __find_from_specific_parent(child_finder: str, from_parent_finder: str) -> str:
    if from_parent_finder is None:
        return child_finder
    return UtilsSetup.finder.by_descendant(
        from_parent_finder,
        child_finder,
    )


def __click_if_element_found(finder: str, click_type: int = __ClickType.CLICK, duration: int = None):
    if finds_some_widgets(finder) is False:
        raise "Cannot not find specific one widget to click"
    if finds_is_tappable(finder) is False:
        raise "Cannot not click element"
    match click_type:
        case __ClickType.CLICK:
            FlutterElement(UtilsSetup.driver, finder).click()
        case __ClickType.DOUBLE_CLICK:
            TouchAction(UtilsSetup.driver).tap(FlutterElement(UtilsSetup.driver, finder), count=2).perform()
        case __ClickType.LONG_CLICK:
            if duration is None:
                TouchAction(UtilsSetup.driver).long_press(FlutterElement(UtilsSetup.driver, finder)).perform()
            else:
                TouchAction(UtilsSetup.driver).long_press(FlutterElement(UtilsSetup.driver, finder),
                                                          duration=duration).perform()
