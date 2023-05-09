import traceback
from setup import UtilsSetup


def finds_some_widgets(finder: str, timeout: int = 1250) -> bool:
    try:
        UtilsSetup.driver.execute_script('flutter:waitFor', finder, timeout)
        return True
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return False


# def finds_nothing(finder: str) -> bool:
#     try:
#         UtilsSetup.driver.execute_script('flutter:waitForAbsent', finder, 40)
#         return False
#     except Exception as e:
#         print(e)
#         print(traceback.format_exc())
#         return True


def finds_is_tappable(finder: str) -> bool:
    try:
        UtilsSetup.driver.execute_script('flutter:waitForTappable', finder, 50)
        return True
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return False
