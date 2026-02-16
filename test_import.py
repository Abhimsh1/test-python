from test-class import TestClass
from os import path, getcwd

print("Current working directory:", getcwd())
print("Path to test_class.py:", path.abspath("test_class.py"))
obj = TestClass()