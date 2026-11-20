from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("Implementation of the abstract method.")

concrete_instance = ConcreteClass()
concrete_instance.abstract_method()  # Output: Implementation of the abstract method.
