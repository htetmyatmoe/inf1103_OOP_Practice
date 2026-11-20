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