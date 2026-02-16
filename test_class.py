from abc import ABC, abstractmethod

class TestClass(ABC):
    @abstractmethod
    def test_method(self):
        pass

obj = TestClass()
obj.test_method()