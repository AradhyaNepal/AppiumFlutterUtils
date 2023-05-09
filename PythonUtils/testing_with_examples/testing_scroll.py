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
    assert False


def going_to_whole_page_vertical(_):
    assert False


def testing_whole_page_scroll_vertical(_):
    assert False


def going_to_whole_page_horizontal(_):
    assert False


def testing_whole_page_scroll_horizontal(_):
    assert False


def going_to_by_type_single_child_vertical(_):
    assert False


def testing_by_type_single_child_scroll_view_vertical(_):
    assert False


def going_to_by_type_single_child_horizontal(_):
    assert False


def testing_by_type_single_child_scroll_view_horizontal(_):
    assert False


def going_to_list_view_vertical(_):
    assert False


def testing_by_type_list_view_vertical(_):
    assert False


def going_to_list_view_horizontal(_):
    assert False


def testing_by_type_list_view_horizontal(_):
    assert False


def going_to_semantic_vertical(_):
    assert False


def testing_semantic_vertical(_):
    assert False


def going_to_semantic_horizontal(_):
    assert False


def testing_semantic_horizontal(_):
    assert False


def going_to_key_vertical(_):
    assert False


def testing_key_vertical(_):
    assert False


def going_to_key_horizontal(_):
    assert False


def testing_key_horizontal(_):
    assert False


if __name__ == "__main__":
    main()
