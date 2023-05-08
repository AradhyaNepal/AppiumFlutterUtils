from setup import UtilsSetup
import traceback


class WhatToWait:
    BY_VALUE_KEY = 1
    BY_TYPE = 2  # Default
    BY_TEXT = 3
    # If semantics causes some error, in Semantic Widget do :
    # excludeSemantics: true or explicitChildNodes:true depending on scenario,
    # View this issue :https://github.com/flutter/flutter/issues/126059
    BY_SEMANTIC_LABEL = 4
    HARD_CODED = 5 # Have no test coverage


def wait(value: str, what_to_wait: int = WhatToWait.BY_TYPE, duration: int = 5000) -> bool:
    print("Waiting For '" + value + "' : To Be Found.")
    return __wait(value, duration, False, what_to_wait)


def wait_for_absence(value: str, what_to_wait: int = WhatToWait.BY_TYPE, duration: int = 5000) -> bool:
    print("Waiting For '" + value + "' : Not To Be Found.")
    return __wait(value, duration, True, what_to_wait)


def __wait(value: str, duration: int, for_absence: bool, what_to_wait: int = WhatToWait.BY_TYPE) -> bool:
    finder = __get_finder(what_to_wait, value)
    try:
        if for_absence:
            UtilsSetup.driver.execute_script('flutter:waitForAbsent', finder, duration)
        else:
            UtilsSetup.driver.execute_script('flutter:waitFor', finder, duration)
        print("Waiting For " + value + " Is Over")
        return True
    except Exception as e:
        print("Error: Waiting For " + value + " Timeout")
        print("For Absence:" + str(for_absence))
        print("\n\n")
        print(e)
        print(traceback.format_exc())
        print("\n\n")
        return False


def __get_finder(how_to_wait, value):
    match how_to_wait:
        case WhatToWait.BY_VALUE_KEY:
            return UtilsSetup.finder.by_value_key(value)
        case WhatToWait.BY_TYPE:
            return UtilsSetup.finder.by_type(value)
        case WhatToWait.BY_TEXT:
            return UtilsSetup.finder.by_text(value)
        case WhatToWait.BY_SEMANTIC_LABEL:
            return UtilsSetup.finder.by_semantics_label(value)
        case WhatToWait.HARD_CODED:
            return value
