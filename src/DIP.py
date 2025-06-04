from abc import ABC, abstractmethod

class Switchable():
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(Switchable):
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


class Fan(Switchable):
    def turn_on(self):
        print("Fan is spinning")

    def turn_off(self):
        print("Fan is stopped")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class TurnOnCommand(Command):
    def __init__(self, device: Switchable):
        self._device = device

    def execute(self):
        self._device.turn_on()


class Button:
    def __init__(self, command: Command):
        self._command = command

    def press(self):
        self._command.execute()


# Usage
light = Light()
fan = Fan()

light_button = Button(TurnOnCommand(light))
fan_button = Button(TurnOnCommand(fan))

light_button.press()
fan_button.press()