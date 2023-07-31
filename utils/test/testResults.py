from utils.test.Constants import TestStatus

class TestResult:
    def __init__(self, test_status: TestStatus):
        self._test_status = test_status


class HttpRequestTestResult(TestResult):
    def __init__(self, test_status, response):
        super().__init__(test_status)
        self.response = response