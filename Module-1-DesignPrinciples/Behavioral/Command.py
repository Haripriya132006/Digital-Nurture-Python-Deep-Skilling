# Commands
class TurnOnCommand:
    def execute(self):
        return "Light is ON"

class TurnOffCommand:
    def execute(self):
        return "Light is OFF"

# Invoker - runs commands
class RemoteControl:
    def press_button(self, command):
        return command.execute()

# Usage
remote = RemoteControl()

print(remote.press_button(TurnOnCommand()))   # Light is ON
print(remote.press_button(TurnOffCommand()))  # Light is OFF