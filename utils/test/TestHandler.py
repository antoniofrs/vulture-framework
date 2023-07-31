import ast
import inspect
import os
from typing import List

from utils.test.TestAnnotation import Test
from utils.test.TestFunction import TestFunction

def get_attributes(keyword):
    if keyword.arg in ('mode', "onFail"):
        return keyword.value.attr
    return ast.literal_eval(keyword.value)


def get_default_values():
    defaults = inspect.signature(Test).parameters.values()
    default_dict = {}
    for param in defaults:
        if param.default != inspect.Parameter.empty:
            default_dict[param.name] = param.default
    return default_dict

def find_decorator_args(decorator: ast.Call):
    decorator_args = get_default_values()
    for keyword in decorator.keywords:
        decorator_args[keyword.arg] = get_attributes(keyword)
    return decorator_args

def get_decorator_if_present(node: ast.FunctionDef , decoratorType):
    for decorator in node.decorator_list:
        if isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name):
            if decorator.func.id == decoratorType.__name__:
                return decorator       
    return None


def get_test_methods(python_file) -> List[TestFunction]:

    try:
        with open(python_file, 'r') as file:
            content = file.read()
            compile(content, python_file, 'exec')
    except Exception as e:
        print(f"Cannot compile {python_file}:  {e}")

    decorated_methods = []

    tree = ast.parse(content)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            decorator = get_decorator_if_present(node, Test)
            if decorator is not None:
                decorator_args = find_decorator_args(decorator)

                file_name = os.path.basename(python_file)
                path = str(python_file).replace(file_name , "")
                module = path.replace("/", ".") + str(file_name).replace(".py", "")

                test_function = TestFunction(
                    module = module,
                    path = path,
                    file_name = file_name,
                    function_name = node.name,
                    test_args = decorator_args
                )

                decorated_methods.append(test_function)

    return decorated_methods


def get_python_files(directory):
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                python_files.append(file_path.replace("\\", "/"))
    return python_files

def find_all_tests() -> List[TestFunction]:
    test_methods = []
    for file in get_python_files("test"):
        for test_method in get_test_methods(file):
            test_methods.append(test_method)
    return test_methods