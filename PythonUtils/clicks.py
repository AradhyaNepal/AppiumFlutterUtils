import time

from setup import UtilsSetup
from appium_flutter_finder import FlutterFinder, FlutterElement
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from finds_widget import *


class WhatToClick:
    ELEVATED_BUTTON = 1
    GESTURE_DETECTOR = 2
    INKWELL = 3
    FLOATING_ACTION_BUTTON = 4
    TEXT_BUTTON = 5
    BY_VALUE_KEY = 6
    BY_TYPE = 7
    BY_TEXT = 8
    # If semantics causes some error, in Semantic Widget do :
    # excludeSemantics: true or explicitChildNodes:true depending on scenario,
    # View this issue :https://github.com/flutter/flutter/issues/126059
    BY_SEMANTIC_LABEL = 9  # Default and recommended
    HARD_CODED = 10 # Have no test coverage


class __ClickType:
    CLICK = 1
    DOUBLE_CLICK = 2
    LONG_CLICK = 3


def click(value: str, what_to_click: int = WhatToClick.BY_SEMANTIC_LABEL):
    __click(value, __ClickType.CLICK, 0, what_to_click)


def double_click(value: str, what_to_click: int = WhatToClick.BY_SEMANTIC_LABEL):
    if what_to_click == WhatToClick.ELEVATED_BUTTON or what_to_click == WhatToClick.TEXT_BUTTON or what_to_click == WhatToClick.FLOATING_ACTION_BUTTON:
        raise "Cannot Double Tap"
    __click(value, __ClickType.DOUBLE_CLICK, 0, what_to_click)


def long_click(value: str, what_to_click: int = WhatToClick.BY_SEMANTIC_LABEL, duration: int = 1000, ):
    if what_to_click == WhatToClick.ELEVATED_BUTTON or what_to_click == WhatToClick.FLOATING_ACTION_BUTTON:
        raise "Cannot Long Tap"
    __click(value, __ClickType.LONG_CLICK, duration, what_to_click)


def __click(value: str, click_type: int, duration: int = 1000,
            what_to_click: int = WhatToClick.BY_SEMANTIC_LABEL):
    match what_to_click:
        case WhatToClick.ELEVATED_BUTTON:
            __click_if_element_found(
                __find_by_text_of_specific_button(value, "ElevatedButton"),
                duration=duration,
                click_type=click_type,
            )
        case WhatToClick.GESTURE_DETECTOR:
            __click_if_element_found(
                __find_by_text_of_specific_button(value, "GestureDetector"),
                duration=duration,
                click_type=click_type,
            )
        case WhatToClick.INKWELL:
            __click_if_element_found(
                __find_by_text_of_specific_button(value, "InkWell"),
                duration=duration,
                click_type=click_type,
            )
        case WhatToClick.FLOATING_ACTION_BUTTON:
            __click_if_element_found(
                UtilsSetup.finder.by_type("FloatingActionButton"),
                duration=duration,
                click_type=click_type,
            )
        case WhatToClick.TEXT_BUTTON:
            __click_if_element_found(
                __find_by_text_of_specific_button(value, "TextButton", ),
                duration=duration,
                click_type=click_type,
            )
        case WhatToClick.BY_VALUE_KEY:
            __click_if_element_found(
                UtilsSetup.finder.by_value_key(value),
                duration=duration,
                click_type=click_type,
            )
        case WhatToClick.BY_TYPE:
            __click_if_element_found(
                UtilsSetup.finder.by_type(value),
                duration=duration,
                click_type=click_type,
            )
        case WhatToClick.BY_TEXT:
            __click_if_element_found(
                UtilsSetup.finder.by_text(value),
                duration=duration,
                click_type=click_type,
            )
        case WhatToClick.BY_SEMANTIC_LABEL:
            __click_if_element_found(
                UtilsSetup.finder.by_semantics_label(value),
                duration=duration,
                click_type=click_type,
            )
        case WhatToClick.HARD_CODED:
            __click_if_element_found(
                value,
                duration=duration,
                click_type=click_type,
            )


def __find_by_text_of_specific_button(value: str, type_of_button: str) -> str:
    return UtilsSetup.finder.by_descendant(
        UtilsSetup.finder.by_type(type_of_button),
        UtilsSetup.finder.by_text(value),
    )


def __click_if_element_found(finder: str, click_type: int = __ClickType.CLICK, duration: int = 1000):
    if finds_some_widgets(finder) is False:
        raise "Cannot not find specific one widget to click"
    if finds_is_tappable(finder) is False:
        raise "Cannot not click element"
    match click_type:
        case __ClickType.CLICK:
            FlutterElement(UtilsSetup.driver, finder).click()
        case __ClickType.DOUBLE_CLICK:
            element = FlutterElement(UtilsSetup.driver, finder)
            element.click()
            time.sleep(0.05)
            element.click()
        case __ClickType.LONG_CLICK:
            TouchAction(UtilsSetup.driver).long_press(FlutterElement(UtilsSetup.driver, finder)).wait(
                duration).release().perform()
            # UtilsSetup.driver.execute_script('flutter:longTap', finder, dict(
            #     durationMilliseconds=duration,
            #     frequency=30
            # ))
