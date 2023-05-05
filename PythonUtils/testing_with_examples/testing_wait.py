import time

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
    group_testing_wait()
    FlutterReportGenerator.generate_report()


def group_testing_wait():
    test(
        "Initial Setup",
        init,
    )
    test(
        "Wait For Value Key to come",
        testing_wait_for_value_key,

    )
    test(
        "Wait For Value Key to go",
        testing_wait_absence_for_value_key,

    )
    test(
        "Wait For Type to come",
        testing_wait_for_type,
    )
    test(
        "Wait For Type to go",
        testing_wait_absence_for_type,
    )
    test(
        "Wait For Text to come",
        testing_wait_for_text,
    )
    test(
        "Wait For Text to go",
        testing_wait_absence_for_text,
    )
    test(
        "Wait For Semantic to come",
        testing_wait_for_semantic,
    )
    test(
        "Wait For Semantic to go",
        testing_wait_absence_for_semantic,
    )
    test(
        "Wait For Hard Coded to come",
        testing_wait_for_hard_coded,
    )
    test(
        "Wait For Hard Coded to go",
        testing_wait_absence_for_hard_coded,
    )
    test(
        "Wait to come till timeout",
        testing_wait_timeout,
    )
    test(
        "Wait to go till timeout",
        testing_absence_timeout,
    )


def testing_wait_for_value_key(_):
    click("ByValueKey")
    find_element_after_wait = wait("by_value_key", HowToWait.BY_VALUE_KEY)
    assert find_element_after_wait


def testing_wait_absence_for_value_key(_):
    click("Reset")
    if finds_some_widgets(UtilsSetup.finder.by_value_key(by_value_key)) is False:
        raise "Cannot find element for which we were waiting"
    do_not_find_element_after_wait = wait_for_absence("by_value_key", HowToWait.BY_VALUE_KEY)
    assert do_not_find_element_after_wait


def testing_wait_for_type(_):
    click("ByType")
    find_element_after_wait = wait("ByTypeWidget")
    assert find_element_after_wait


def testing_wait_absence_for_type(_):
    click("Reset")
    if finds_some_widgets(UtilsSetup.finder.by_type("ByTypeWidget")) is False:
        raise "Cannot find element for which we were waiting"
    do_not_find_element_after_wait = wait_for_absence("ByTypeWidget")
    assert do_not_find_element_after_wait


def testing_wait_for_text(_):
    click("ByText")
    find_element_after_wait = wait("ByText", HowToWait.BY_TEXT)
    assert find_element_after_wait


def testing_wait_absence_for_text(_):
    click("Reset")
    if finds_some_widgets(UtilsSetup.finder.by_text("ByText")) is False:
        raise "Cannot find element for which we were waiting"
    do_not_find_element_after_wait = wait_for_absence("ByText", HowToWait.BY_TEXT)
    assert do_not_find_element_after_wait


def testing_wait_for_semantic(_):
    click("BySemanticLabel")
    find_element_after_wait = wait("BySemanticLabelOutput", HowToWait.BY_SEMANTIC_LABEL)
    assert find_element_after_wait is False
    time.sleep(0.5)


def testing_wait_absence_for_semantic(_):
    click("Reset")
    if finds_some_widgets(UtilsSetup.finder.by_semantics_label("BySemanticLabelOutput")) is False:
        raise "Cannot find element for which we were waiting"
    do_not_find_element_after_wait = wait_for_absence("BySemanticLabelOutput", HowToWait.BY_SEMANTIC_LABEL)
    assert do_not_find_element_after_wait is False


def get_hard_coded() -> str:
    return UtilsSetup.finder.by_descendant(
        UtilsSetup.finder.by_ancestor(
            UtilsSetup.finder.by_semantics_label("ByHardCodedOutput"),
            UtilsSetup.finder.by_type("Row")
        ),
        UtilsSetup.finder.by_type("ByTypeWidget"),
    )


def testing_wait_for_hard_coded(_):
    click("ByHardCoded")
    find_element_after_wait = wait(get_hard_coded(), HowToWait.HARD_CODED)
    assert find_element_after_wait


def testing_wait_absence_for_hard_coded(_):
    click("Reset")
    if finds_some_widgets(get_hard_coded()) is False:
        raise "Cannot find element for which we were waiting"
    do_not_find_element_after_wait = wait_for_absence(get_hard_coded(), HowToWait.HARD_CODED)
    assert do_not_find_element_after_wait


def testing_wait_timeout(_):
    click("TimeOut")
    find_element_after_wait = wait("TimeOutOutput", HowToWait.BY_SEMANTIC_LABEL)
    assert find_element_after_wait


def testing_absence_timeout(_):
    click("Reset")
    if finds_some_widgets(UtilsSetup.finder.by_semantics_label("TimeOutOutput")) is False:
        raise "Cannot find element for which we were waiting"
    do_not_find_element_after_wait = wait_for_absence("TimeOutOutput", HowToWait.BY_SEMANTIC_LABEL)
    assert do_not_find_element_after_wait


def init(_):
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("/WaitTestScreen")).click()
    UtilsSetup.driver.execute_script('flutter:waitFor', UtilsSetup.finder.by_type("WaitTestScreen"), 1500)
    finds_reset_output()


def reset():
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("reset")).click()
    finds_reset_output()


def finds_reset_output():
    assert finds_some_widgets(UtilsSetup.finder.by_semantics_label("ResetOutputBox"))


if __name__ == "__main__":
    main()
