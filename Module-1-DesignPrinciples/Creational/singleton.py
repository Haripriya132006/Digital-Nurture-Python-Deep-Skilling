class Logger:
    _logs = []
    
    def log(self, message):
        Logger._logs.append(message)
        print(f"Logged: {message}")
    
    def show_all(self):
        print(f"\nAll Logs: {Logger._logs}\n")

# Create first logger
logger1 = Logger()
logger1.log("User logged in")
logger1.show_all()

# Create second logger
logger2 = Logger()
logger2.log("Database connected")
logger2.show_all()  # Shows BOTH logs!

print(f"Same logs? {logger1._logs is logger2._logs}")  # True