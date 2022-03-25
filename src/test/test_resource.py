import unittest
from fastapi.testclient import TestClient

import controller.resource as resource


# test cases for resource controller
class TestResource(unittest.TestCase):
    client = TestClient(resource.app)

    key_value = {
        "key": "dummy key",
        "value": "dummy value"
    }

    wrong_key_value = {
        "wrong key": "wrong value"
    }

    def test_get(self):
        result = self.client.get("/key_value")
        assert result.status_code == 200

    def test_post(self):
        result = self.client.post("/key_value", json=self.key_value)
        assert result.status_code == 200

    def test_post_unprocessable(self):
        result = self.client.post("/key_value", json=self.wrong_key_value)
        assert result.status_code == 422

