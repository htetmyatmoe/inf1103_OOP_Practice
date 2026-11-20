from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass

class canspeak(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal, canspeak):
    def make_sound(self):
        print("Woof!")
    def walk(self):
        print("Dog is walking.")

class Cat(Animal, canspeak):
    def make_sound(self):
        print("Meow!")
    def walk(self):
        print("Cat is walking.")

dog = Dog()
cat = Cat()

dog.make_sound()  # Output: Woof!
cat.make_sound()  # Output: Meow!
dog.walk()  # Output: Dog is walking.
cat.walk()  # Output: Cat is walking.