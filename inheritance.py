from pytest import Class


class RobotPapa:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def greet(self):
        print(f"Hello, I am {self.name}. My energy level is {self.energy}.")

class RobotChild(RobotPapa): 
    def __init__(self, name, energy, toy):
        super().__init__(name, energy)
        self.toy = toy

    def greet(self):
        print(f"Hi, I am {self.name}. My energy level is {self.energy}. I love playing with my {self.toy}.")

    def play(self):
        print(f"{self.name} is playing with {self.toy}. Energy level: {self.energy}")

robot_papa = RobotPapa("RoboDad", 100)
robot_child = RobotChild("RoboKid", 80, "ball")

robot_papa.greet()  # Output: Hello, I am RoboDad. My energy level is 100.
robot_child.greet()  # Output: Hi, I am RoboKid. My energy level is 80. I love playing with my ball.
robot_child.play()  # Output: RoboKid is playing with ball. Energy level:


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, s):
        self.s = s
    def area(self,scale):
        return self.s ** 2 * scale

#for shape in [Shape(), Square(2)]:
 #   print(shape.area())


class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        return f"{self.name} is eating"
    def sleep(self):
        return f"{self.name} is sleeping"

class Dog(Animal):
    def __init__(self, breed):
        #super().__init__("Dog")
        self.breed = breed
    def bark(self):
        return "Woof"

d = Dog("Golden Retriever")
print(d.eat())     # Dog is eating   ← inherited, no super() needed
print(d.sleep())   # Dog is sleeping ← inherited
print(d.bark())    # Woof            ← Dog's own
print(d.breed)   # Golden Retriever ← Dog's own


