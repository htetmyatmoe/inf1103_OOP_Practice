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

class device (ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Computer(device):
    def start(self):
       print("Computer is starting.")

class Smartphone(Computer):

    def stop(self):
        print("Smartphone is stopping.")

Smartphone().stop()  # Output: Smartphone is stopping.