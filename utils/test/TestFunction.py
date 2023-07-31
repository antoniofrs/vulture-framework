class TestFunction:
    def __init__(self, path: str, module: str, file_name: str, function_name, test_args):
        self.path = path
        self.module = module
        self.file_name = file_name
        self.function_name = function_name
        self.test_args = test_args

    def __str__(self):
        attribute_list = ", ".join([f"{attr}={getattr(self, attr)}" for attr in self.__dict__])
        return f"TestFunction({attribute_list})"