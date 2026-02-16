from test_class import TestClass
from os import path, getcwd

print("Current working directory:", getcwd())
print("Path to test_class.py:", path.abspath("test_class.py"))


class TestClass(TestClass):
    def test_method(self):
        print("Implementation of test_method")

obj = TestClass()