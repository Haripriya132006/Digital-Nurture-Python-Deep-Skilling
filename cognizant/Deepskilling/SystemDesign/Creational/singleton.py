
# ============================================================================
# THE SINGLETON LOGGER CLASS
# ============================================================================
class Logger:

    _shared_logs = []

    def __init__(self, name="AppLogger"):
        self.name = name

    def log(self, level, message):
        """Formats and stores the log in the shared list."""
        log_entry = f"[[{level}] {message}"
        
        # Append to the shared class-level list
        Logger._shared_logs.append(log_entry)
        # print(f"  {log_entry}")

    def info(self, message):
        self.log("INFO", message)

    def warning(self, message):
        self.log("WARNING", message)

    def print_all_logs(self):
        print(f"\n--- ALL LOGS STORED IN SHARD STORE ---")
        for log in Logger._shared_logs:
            print(f"  {log}")
        print(f"Total logs captured: {len(Logger._shared_logs)}\n---------------------------------------")




logger_part_one = Logger()
logger_part_one.info("User 'admin' logged in.")

logger_part_one.print_all_logs()

logger_part_two = Logger()
logger_part_two.warning("Database connection is slow.")
logger_part_two.info("Payment processed successfully.")

logger_part_two.print_all_logs()