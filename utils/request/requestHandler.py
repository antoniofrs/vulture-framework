from enum import Enum
import requests
from utils.test.Constants import TestStatus


class Method(Enum):
    GET = requests.get
    POST = requests.post
    PUT = requests.put
    DELETE = requests.delete


class HttpRequest:
    def __init__(self):
        self._url = "http://localhost:80"
        self._method = Method.GET
        self._headers = []
        self._body = {}

    @staticmethod
    def testThat():
        return HttpRequest()


    def url(self, url):
        self._url = url
        return self

    def method(self, method):
        self._method = method
        return self

    def header(self, name, value):
        self._headers.append({name: value})
        return self

    def body(self, body):
        self._body = body
        return self

    def executeRequest(self):
        common_params = {
            "url": self._url,
            "json": self._body,
            "headers": self._headers
        }

        try:
            self._method(**common_params)
        except requests.exceptions.RequestException:
            print("The request could not be sent")
            return TestStatus.EXCEPTION


        
