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
    group_testing_scroll()
    FlutterReportGenerator.generate_report()


def group_testing_scroll():
    test(
        "Initial Setup",
        init,
    )
    test(
        "Going to Whole Page Scrolling Vertical",
        going_to_whole_page_vertical,
    )
    test(
        "Whole Page Scrolling Vertical",
        testing_whole_page_scroll_vertical,
    )
    test(
        "Going to Whole Page Scrolling Horizontal",
        going_to_whole_page_horizontal,
    )
    test(
        "Whole Page Scrolling Horizontal",
        testing_whole_page_scroll_horizontal,
    )
    test(
        "Going To By Type SingleChildScrollView Scrolling Vertical",
        going_to_by_type_single_child_vertical,
    )
    test(
        "By Type SingleChildScrollView Scrolling Vertical",
        testing_by_type_single_child_scroll_view_vertical,
    )
    test(
        "Going To By Type SingleChildScrollView Scrolling Horizontal",
        going_to_by_type_single_child_horizontal,
    )
    test(
        "By Type SingleChildScrollView Scrolling Horizontal",
        testing_by_type_single_child_scroll_view_horizontal,
    )
    test(
        "Going To ListView Vertical",
        going_to_list_view_vertical,
    )
    test(
        "By Type ListView Scrolling Vertical",
        testing_by_type_list_view_vertical,
    )
    test(
        "Going To ListView Horizontal",
        going_to_list_view_horizontal
    )
    test(
        "By Type ListView Scrolling Horizontal",
        testing_by_type_list_view_horizontal,
    )
    test(
        "Going To Semantic Vertical",
        going_to_semantic_vertical,
    )
    test(
        "By Semantic Scrolling Vertical",
        testing_semantic_vertical,
    )
    test(
        "Going To Semantic Horizontal",
        going_to_semantic_horizontal,
    )
    test(
        "By Semantic Scrolling Horizontal",
        testing_semantic_horizontal,
    )
    test(
        "Going To Key Vertical",
        going_to_key_vertical,
    )
    test(
        "By ValueKey Scrolling Vertical",
        testing_key_vertical,
    )
    test(
        "Going To Key Horizontal",
        going_to_key_horizontal,
    )
    test(
        "By ValueKey Scrolling Horizontal",
        testing_key_horizontal,
    )


def init(_):
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("/ScrollTestScreen")).click()
    assert finds_some_widgets(UtilsSetup.finder.by_type("ScrollTestScreen"))


def going_to_whole_page_vertical(_):
    click("/ScrollMaterialScreen")
    assert finds_some_widgets(UtilsSetup.finder.by_type("ScrollMaterialScreen"))


def testing_whole_page_scroll_vertical(_):
    __finds_start_assert()
    scroll(go_down_percentage=100)
    __finds_mid_assert()
    scroll(go_down_percentage=100)
    __finds_end_assert()


def going_to_whole_page_horizontal(_):
    click("axis_swift", what_to_click=WhatToClick.BY_VALUE_KEY)


def testing_whole_page_scroll_horizontal(_):
    __finds_start_assert()
    scroll(go_right_percentage=100)
    __finds_mid_assert()
    scroll(go_right_percentage=100)
    __finds_end_assert()


def going_to_by_type_single_child_vertical(_):
    __go_back()
    click("/ScrollByTypeScreen")
    assert finds_some_widgets(UtilsSetup.finder.by_type("ScrollByTypeScreen"))


def testing_by_type_single_child_scroll_view_vertical(_):
    __finds_start_assert()
    scroll(go_down_percentage=100, what_to_scroll="SingleChildScrollView", scroll_type=ScrollType.BY_TYPE)
    __finds_mid_assert()
    scroll(go_down_percentage=100, what_to_scroll="SingleChildScrollView", scroll_type=ScrollType.BY_TYPE)
    __finds_end_assert()


def going_to_by_type_single_child_horizontal(_):
    click("axis_swift", what_to_click=WhatToClick.BY_VALUE_KEY)


def testing_by_type_single_child_scroll_view_horizontal(_):
    __finds_start_assert()
    scroll(go_right_percentage=100, what_to_scroll="SingleChildScrollView", scroll_type=ScrollType.BY_TYPE)
    __finds_mid_assert()
    scroll(go_right_percentage=100, what_to_scroll="SingleChildScrollView", scroll_type=ScrollType.BY_TYPE)
    __finds_end_assert()


def going_to_list_view_vertical(_):
    click("axis_swift", what_to_click=WhatToClick.BY_VALUE_KEY)
    click("type_swift", what_to_click=WhatToClick.BY_VALUE_KEY)


def testing_by_type_list_view_vertical(_):
    __finds_start_assert()
    scroll(go_down_percentage=100, what_to_scroll="ListView", scroll_type=ScrollType.BY_TYPE)
    __finds_mid_assert()
    scroll(go_down_percentage=100, what_to_scroll="ListView", scroll_type=ScrollType.BY_TYPE)
    __finds_end_assert()


def going_to_list_view_horizontal(_):
    click("axis_swift", what_to_click=WhatToClick.BY_VALUE_KEY)


def testing_by_type_list_view_horizontal(_):
    __finds_start_assert()
    scroll(go_right_percentage=100, what_to_scroll="ListView", scroll_type=ScrollType.BY_TYPE)
    __finds_mid_assert()
    scroll(go_right_percentage=100, what_to_scroll="ListView", scroll_type=ScrollType.BY_TYPE)
    __finds_end_assert()


def going_to_semantic_vertical(_):
    __go_back()
    click("/ScrollBySemanticScreen")


def testing_semantic_vertical(_):
    __finds_start_assert()
    scroll(go_down_percentage=100, what_to_scroll="SingleChildScrollView", scroll_type=ScrollType.BY_SEMANTIC)
    __finds_mid_assert()
    scroll(go_down_percentage=100, what_to_scroll="SingleChildScrollView", scroll_type=ScrollType.BY_SEMANTIC)
    __finds_end_assert()


def going_to_semantic_horizontal(_):
    click("axis_swift", what_to_click=WhatToClick.BY_VALUE_KEY)


def testing_semantic_horizontal(_):
    __finds_start_assert()
    scroll(go_right_percentage=100, what_to_scroll="SingleChildScrollView", scroll_type=ScrollType.BY_SEMANTIC)
    __finds_mid_assert()
    scroll(go_right_percentage=100, what_to_scroll="SingleChildScrollView", scroll_type=ScrollType.BY_SEMANTIC)
    __finds_end_assert()


def going_to_key_vertical(_):
    __go_back()
    click("/ScrollByKeyScreen")


def testing_key_vertical(_):
    __finds_start_assert()
    scroll(go_down_percentage=100, what_to_scroll="single_child_scroll_view", scroll_type=ScrollType.BY_KEY)
    __finds_mid_assert()
    scroll(go_down_percentage=100, what_to_scroll="single_child_scroll_view", scroll_type=ScrollType.BY_KEY)
    __finds_end_assert()


def going_to_key_horizontal(_):
    click("axis_swift", what_to_click=WhatToClick.BY_VALUE_KEY)


def testing_key_horizontal(_):
    __finds_start_assert()
    scroll(go_right_percentage=100, what_to_scroll="single_child_scroll_view", scroll_type=ScrollType.BY_KEY)
    __finds_mid_assert()
    scroll(go_right_percentage=100, what_to_scroll="single_child_scroll_view", scroll_type=ScrollType.BY_KEY)
    __finds_end_assert()


def __go_back():
    UtilsSetup.driver.switch_to.context("NATIVE_APP")
    UtilsSetup.driver.back()
    UtilsSetup.driver.switch_to.context("FLUTTER")


def __finds_start_assert():
    assert finds_some_widgets(UtilsSetup.finder.by_value_key("start_key"), timeout=50)
    assert finds_some_widgets(UtilsSetup.finder.by_value_key("mid_key"), timeout=50) is False
    assert finds_some_widgets(UtilsSetup.finder.by_value_key("end_key"), timeout=50) is False


def __finds_mid_assert():
    assert finds_some_widgets(UtilsSetup.finder.by_value_key("start_key"), timeout=50) is False
    assert finds_some_widgets(UtilsSetup.finder.by_value_key("mid_key"), timeout=50)
    assert finds_some_widgets(UtilsSetup.finder.by_value_key("end_key"), timeout=50) is False


def __finds_end_assert():
    assert finds_some_widgets(UtilsSetup.finder.by_value_key("start_key"), timeout=50) is False
    assert finds_some_widgets(UtilsSetup.finder.by_value_key("mid_key"), timeout=50) is False
    assert finds_some_widgets(UtilsSetup.finder.by_value_key("end_key"), timeout=50)


if __name__ == "__main__":
    main()
