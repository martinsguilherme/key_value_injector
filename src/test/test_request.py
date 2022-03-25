import unittest

import model.request as request


# test cases for request model
class TestRequest(unittest.TestCase):
    key = "dummy key"
    value = "dummy value"

    key_value = {
        "key": "dummy key",
        "value": "dummy value"
    }

    def test_create(self):
        result = request.Request(key=self.key, value=self.value)
        self.assertIsNotNone(result)

    def test_get_key_value(self):
        result = request.Request(key=self.key, value=self.value)
        self.assertIsNotNone(result.get_key_value())
