from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# Concrete Commands
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()

# Receiver
class Light:
    def __init__(self, location):
        self.location = location
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.location} light is ON")

    def turn_off(self):
        self.is_on = False
        print(f"{self.location} light is OFF")

# Invoker
class RemoteControl:
    def __init__(self):
        self.commands = {}
        self.history = []

    def set_command(self, button, command):
        self.commands[button] = command

    def press_button(self, button):
        if button in self.commands:
            self.commands[button].execute()
            self.history.append(self.commands[button])

    def undo(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()

# Client code
def main():
    # Create receivers
    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")

    # Create commands
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    # Create invoker
    remote = RemoteControl()

    # Set up commands
    remote.set_command("living_room_on", living_room_light_on)
    remote.set_command("living_room_off", living_room_light_off)
    remote.set_command("kitchen_on", kitchen_light_on)
    remote.set_command("kitchen_off", kitchen_light_off)

    # Use the remote
    remote.press_button("living_room_on")  # Living Room light is ON
    remote.press_button("kitchen_on")      # Kitchen light is ON
    remote.undo()                          # Kitchen light is OFF
    remote.press_button("living_room_off") # Living Room light is OFF

if __name__ == "__main__":
    main()