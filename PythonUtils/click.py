from setup import UtilsSetup
from appium_flutter_finder import FlutterFinder, FlutterElement
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from finds_widget import *


class HowToClick:
    ELEVATED_BUTTON = 1
    GESTURE_DETECTOR = 2
    INKWELL = 3
    FLOATING_ACTION_BUTTON = 4
    TEXT_BUTTON = 5
    # ICON_BUTTON = 6
    BY_VALUE_KEY = 7
    BY_TYPE = 8
    BY_TEXT = 9
    BY_SEMANTIC_LABEL = 10  # Default and recommended
    # BY_SEMANTIC_LABEL_CHILD = 11


def click(value: str, how_to_click: HowToClick = HowToClick.BY_SEMANTIC_LABEL, from_parent_finder: str = None, ):
    match how_to_click:
        case HowToClick.ELEVATED_BUTTON:
            __click_if_element_found(
                __find_by_text_of_specific_type_of_button_and_from_specific_parent(value, "ElevatedButton",
                                                                                   from_parent_finder),
            )
        case HowToClick.GESTURE_DETECTOR:
            __click_if_element_found(
                __find_by_text_of_specific_type_of_button_and_from_specific_parent(value, "GestureDetector",
                                                                                   from_parent_finder)
            )
        case HowToClick.INKWELL:
            __click_if_element_found(
                __find_by_text_of_specific_type_of_button_and_from_specific_parent(value, "InkWell", from_parent_finder)
            )
        case HowToClick.FLOATING_ACTION_BUTTON:
            __click_if_element_found(
                __find_from_specific_parent(
                    UtilsSetup.finder.by_type("FloatingActionButton"),
                    from_parent_finder,
                )
            )
        case HowToClick.TEXT_BUTTON:
            __click_if_element_found(
                __find_by_text_of_specific_type_of_button_and_from_specific_parent(value, "TextButton",
                                                                                   from_parent_finder)
            )
        case HowToClick.BY_VALUE_KEY:
            __click_if_element_found(
                __find_from_specific_parent(
                    UtilsSetup.finder.by_value_key(value),
                    from_parent_finder,
                )
            )
        case HowToClick.BY_TYPE:
            __click_if_element_found(
                __find_from_specific_parent(
                    UtilsSetup.finder.by_type(value),
                    from_parent_finder,
                ),
            )
        case HowToClick.BY_TEXT:
            __click_if_element_found(
                __find_from_specific_parent(
                    UtilsSetup.finder.by_text(value),
                    from_parent_finder,
                ),
            )
        case HowToClick.BY_SEMANTIC_LABEL:
            __click_if_element_found(
                __find_from_specific_parent(
                    UtilsSetup.finder.by_semantics_label(value),
                    from_parent_finder,
                ),
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


def __click_if_element_found(finder: str):
    if finds_some_widgets(finder) is False:
        raise "Cannot not find specific one widget to click"
    if finds_is_tappable(finder) is False:
        raise "Cannot not click element"
    FlutterElement(UtilsSetup.driver, finder).click()


def double_click(value: str, how_to_click: HowToClick = HowToClick.BY_SEMANTIC_LABEL,
                 identifier_added_to_child: bool = False):
    print("Hello")


def long_click(value: str, how_to_click: HowToClick = HowToClick.BY_SEMANTIC_LABEL,
               duration_in_milliseconds: int = None, identifier_added_to_child: bool = False):
    print("Hello")
