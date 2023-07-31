import importlib
from utils.test.TestFunction import TestFunction


def execute_test(test_function: TestFunction):

    module = test_function.module
    function_name = test_function.function_name

    try:
        mod = importlib.import_module(module)
        func = getattr(mod, function_name)
        return func()
    except Exception as e:
        print(f"Impossibile importare il modulo {module}: {e}")