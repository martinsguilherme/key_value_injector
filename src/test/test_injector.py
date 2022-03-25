import unittest

import model.injector as injector


# test cases for injector model
class TestInjector(unittest.TestCase):

    def test_create(self):
        result = injector.Injector()
        self.assertIsNotNone(result)

    def test_get_key_value(self):
        result = injector.Injector()
        self.assertIsNotNone(result.get_value())
