from utils.test.Constants import OnFail, TestStatus
from utils.test.testResults import TestResult


def Test(name="", onFail=OnFail.STOP_CURRENT, foundThat =[], willEnsureThat =[]):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if not isinstance(result, TestResult):
                return TestResult(TestStatus.EXCEPTION)

            return result

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__annotations__ = func.__annotations__

        return wrapper

    return decorator
