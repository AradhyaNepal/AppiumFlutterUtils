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
    group_testing_enter_text()
    FlutterReportGenerator.generate_report()


def group_testing_enter_text():
    test(
        "Initial Setup",
        init,
    )
    test(
        "Testing Label in TextField",
        testing_label_text_field,
    )
    test(
        "Testing Label in TextFormField",
        testing_label_text_form_field,
    )
    test(
        "Testing Key in TextField",
        testing_key_text_field,
    ),
    test(
        "Testing Key in TextFormField",
        testing_key_text_form_field,
    ),
    test(
        "Testing Type in TextField",
        testing_type_text_field,
    ),
    test(
        "Testing Type in TextFormField",
        testing_type_text_form_field,
    ),
    test(
        "Testing Semantic in TextField",
        testing_semantic_text_field,
    ),
    test(
        "Testing Semantic in TextFormField",
        testing_semantic_text_form_field,
    ),


def testing_label_text_field(_):
    reset()
    enter_text("ByLabelTextField", "ByLabelTextField")
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is ByLabelTextField"))


def testing_label_text_form_field(_):
    reset()
    enter_text("ByLabelTextFormField", "ByLabelTextFormField")
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is ByLabelTextFormField"))


def testing_key_text_field(_):
    reset()
    enter_text("by-value-key_text_field", "by-value-key_text_field", where_type=WhereType.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is by-value-key_text_field"))


def testing_key_text_form_field(_):
    reset()
    enter_text("by-value-key_text_form_field", "by-value-key_text_form_field", where_type=WhereType.BY_VALUE_KEY)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is by-value-key_text_form_field"))


def testing_type_text_field(_):
    reset()
    enter_text("ByTypeTextField", "ByTypeTextField", where_type=WhereType.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is ByTypeTextField"))


def testing_type_text_form_field(_):
    reset()
    enter_text("ByTypeTextFormField", "ByTypeTextFormField", where_type=WhereType.BY_TYPE)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is ByTypeTextFormField"))


def testing_semantic_text_field(_):
    reset()
    enter_text("BySemanticTextField", "BySemanticTextField", where_type=WhereType.BY_SEMANTIC_LABEL)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is BySemanticTextField"))


def testing_semantic_text_form_field(_):
    reset()
    enter_text("BySemanticTextFormField", "BySemanticTextFormField", where_type=WhereType.BY_SEMANTIC_LABEL)
    assert finds_some_widgets(UtilsSetup.finder.by_text("Output is BySemanticTextFormField"))


def init(_):
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("/EnterTextTestScreen")).click()
    UtilsSetup.driver.execute_script('flutter:waitFor', UtilsSetup.finder.by_type("EnterTextTestScreen"), 1500)
    finds_reset_output()


def reset():
    FlutterElement(UtilsSetup.driver, UtilsSetup.finder.by_value_key("reset")).click()
    finds_reset_output()


def finds_reset_output():
    assert finds_some_widgets(UtilsSetup.finder.by_text("No Output"))


if __name__ == "__main__":
    main()
