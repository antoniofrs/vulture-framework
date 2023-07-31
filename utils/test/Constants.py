from enum import Enum


class TestStatus(Enum):
    SUCCESS = "Success"
    FAILED = "Failed"
    EXCEPTION = "Exception"

class TestMode(Enum):
    ASYNCRONOUS = "async"
    SYNCHRONOUS = "Failed"    

class OnFail(Enum):
    CONTINUE = "continue"
    STOP_CURRENT = "stopCurrent"
    STOP_ALL = "stopAll" 