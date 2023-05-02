class HowToClick:
    ELEVATED_BUTTON = 1
    GESTURE_DETECTOR = 2
    INKWELL = 3
    FLOATING_ACTION_BUTTON = 4
    TEXT_BUTTON = 5
    ICON_BUTTON = 6

    BY_VALUE_KEY = 7
    BY_TYPE = 8
    BY_TEXT = 9
    BY_SEMANTIC_LABEL = 10  # Default and recommended


def click(value: str, how_to_click: HowToClick = HowToClick.BY_SEMANTIC_LABEL, identifier_added_to_child: bool = False):
    print("Hello")


def double_click(value: str, how_to_click: HowToClick = HowToClick.BY_SEMANTIC_LABEL,
                 identifier_added_to_child: bool = False):
    print("Hello")


def long_click(value: str, how_to_click: HowToClick = HowToClick.BY_SEMANTIC_LABEL,
               duration_in_milliseconds: int = None, identifier_added_to_child: bool = False):
    print("Hello")
