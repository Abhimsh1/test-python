from test_class import TestClass
from os import path, getcwd

print("Current working directory:", getcwd())
print("Path to test_class.py:", path.abspath("test_class.py"))


class TestClassImpl(TestClass):
    def test_method(self):
        print("Implementation of test_method")


with open("test_class.txt", "r") as file:
    file_content = file.read()
    print("Content of test_class.txt:")

obj = TestClassImpl()
obj.test_method()
