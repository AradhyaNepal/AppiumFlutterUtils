from setup import UtilsSetup
from finds_widget import *
from appium_flutter_finder import *


class WhereType:
    BY_LABEL = 1  # Third Recommended
    BY_VALUE_KEY = 2  # Second Recommended
    BY_TYPE = 3
    # If semantics causes some error, in Semantic Widget do :
    # excludeSemantics: true or explicitChildNodes:true depending on scenario,
    # View this issue :https://github.com/flutter/flutter/issues/126059
    BY_SEMANTIC_LABEL = 4  # Default and Recommended
    HARD_CODED = 5  # Have No Test Coverage


def enter_text(what_to_enter: str, where_to_enter: str, where_type: int = WhereType.BY_LABEL):
    match where_type:
        case WhereType.BY_LABEL:
            __check_and_enter_text(
                what_to_enter,
                UtilsSetup.finder.by_ancestor(
                    UtilsSetup.finder.by_text(where_to_enter),
                    UtilsSetup.finder.by_type("TextField"),
                ),
            )
        case WhereType.BY_VALUE_KEY:
            __check_and_enter_text(
                what_to_enter,
                UtilsSetup.finder.by_value_key(where_to_enter),
            )
        case WhereType.BY_TYPE:
            __check_and_enter_text(
                what_to_enter,
                UtilsSetup.finder.by_type(where_to_enter),
            )
        case WhereType.BY_SEMANTIC_LABEL:
            __check_and_enter_text(
                what_to_enter,
                UtilsSetup.finder.by_semantics_label(where_to_enter),
            )
        case WhereType.HARD_CODED:
            __check_and_enter_text(
                what_to_enter,
                where_to_enter,
            )


def __check_and_enter_text(value: str, finder: str):
    if finds_some_widgets(finder) is False:
        raise "Element Not found"
    FlutterElement(UtilsSetup.driver, finder).send_keys(value)
