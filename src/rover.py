from abc import ABC, abstractmethod

class LunarVehicleInterface(ABC):
    @abstractmethod
    def go_forward(self, distance):
        pass

    @abstractmethod
    def go_backward(self, distance):
        pass

    @abstractmethod
    def rotate(self, direction):
        pass

    @abstractmethod
    def turn_right(self, angle):
        pass

    @abstractmethod
    def turn_left(self, angle):
        pass

    @abstractmethod
    def start_point(self):
        pass

    @abstractmethod
    def location(self):
        pass

class Rover(LunarVehicleInterface):
    def __init__(self, start_location, start_rotation):
        self.x, self.y = start_location
        self.rotation = start_rotation
        self.s_x, self.s_y = start_location
        self.s_rotation = start_rotation

    def go_forward(self, distance):
        self.x += distance
        print("Going forward")

    def go_backward(self, distance):
        self.x -= distance
        print("Going backward")

    def rotate(self, direction):
        print("Rotating")
        if direction == "left":
            self.rotation -= 90
        elif direction == "right":
            self.rotation += 90

    def turn_right(self, angle):
        self.rotation += angle
        print("Turning right", angle)
        
    def turn_left(self, angle):
        self.rotation -= angle
        print("Turning left", angle)

    def start_point(self):
        print("Starting point is:", self.s_x, self.s_y)
        print("Starting rotation is:", self.s_rotation)

    def location(self):
        print("Current location is:", self.x, self.y)
        print("Current rotation is:", self.rotation)
