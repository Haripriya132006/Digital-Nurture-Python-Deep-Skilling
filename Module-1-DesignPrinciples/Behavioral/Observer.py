# Subject - the object being observed
class WeatherStation:
    def __init__(self):
        self.observers = []
    
    def register_observer(self, observer):
        self.observers.append(observer)  # Subscribe
    
    def set_temperature(self, temp):
        for observer in self.observers:
            observer.update(temp)  # Notify all observers

# Observer 1
class PhoneDisplay:
    def update(self, temperature):
        print(f"Phone: {temperature}°C")

# Observer 2
class WebDisplay:
    def update(self, temperature):
        print(f"Web: {temperature}°C")

# Usage
station = WeatherStation()
station.register_observer(PhoneDisplay())
station.register_observer(WebDisplay())

station.set_temperature(25)
# Output:
# Phone: 25°C
# Web: 25°C

station.set_temperature(30)
# Output:
# Phone: 30°C
# Web: 30°C