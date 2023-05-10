from setup import UtilsSetup
from finds_widget import finds_some_widgets


class ScrollType:
    WHOLE_SCREEN = 1  # Default
    BY_SEMANTIC = 2
    BY_TYPE = 3
    BY_KEY = 4


def scroll(go_down_percentage: float = 0, go_right_percentage: float = 0, what_to_scroll: str = None,
           scroll_type: int = ScrollType.WHOLE_SCREEN):
    value = UtilsSetup.driver.execute_script('flutter:getCenter', UtilsSetup.finder.by_type("MaterialApp"))
    dx_center = value["dx"]
    dy_center = value["dy"]
    dx_total = dx_center * 2
    dy_total = dy_center * 2
    go_down_value = dx_total * (go_down_percentage / 100)
    go_right_value = dy_total * (go_right_percentage / 100)
    scroll_value = dict(
        dx=-go_right_value,
        dy=-go_down_value,
        durationMilliseconds=100,
        frequency=30,
    )
    match scroll_type:
        case ScrollType.WHOLE_SCREEN:
            UtilsSetup.driver.execute_script('flutter:scroll', UtilsSetup.finder.by_type('MaterialApp'), scroll_value)
        case ScrollType.BY_SEMANTIC:
            __no_value_found_check(what_to_scroll)
            __scroll_if_found(UtilsSetup.finder.by_semantics_label(what_to_scroll), scroll_value)
        case ScrollType.BY_TYPE:
            __no_value_found_check(what_to_scroll)
            __scroll_if_found(UtilsSetup.finder.by_type(what_to_scroll), scroll_value)
        case ScrollType.BY_KEY:
            __no_value_found_check(what_to_scroll)
            __scroll_if_found(UtilsSetup.finder.by_value_key(what_to_scroll), scroll_value)


def __no_value_found_check(what_to_scroll: str):
    if what_to_scroll is None:
        raise "Please pass what to scroll"


def __scroll_if_found(finder: str, scroll_value: dict):
    if finds_some_widgets(finder) is False:
        raise "Nothing Found To Scroll"
    UtilsSetup.driver.execute_script('flutter:scroll', finder, scroll_value)
