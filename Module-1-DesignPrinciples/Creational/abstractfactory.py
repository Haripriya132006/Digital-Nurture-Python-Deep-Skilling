from abc import ABC, abstractmethod

class Ui(ABC):
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def view(self):
        pass


class LightUi(Ui):
    def render(self):
        print("Rendering light ui")
    
    def view(self):
        print("Viewing website in light ui")


class DarkUi(Ui):
    def render(self):
        print("Rendering dark ui")
    
    def view(self):
        print("Viewing website in dark ui")


class UiFactory:
    @staticmethod
    def factory(ui_type):
        if ui_type == "light":
            return LightUi()
        elif ui_type == "dark":
            return DarkUi()
        else:
            raise ValueError(f"Unknown UI type: {ui_type}")


def main():
    type=input("Enter the type: ")
    ui=UiFactory.factory(type.lower())
    ui.render()
    ui.view()

main()