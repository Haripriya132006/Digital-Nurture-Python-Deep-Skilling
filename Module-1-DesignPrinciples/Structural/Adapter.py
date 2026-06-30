# Old class with different interface
class OldPrinter:
    def print_text(self, text):
        return f"Old Printer: {text}"

# New class with different interface
class NewPrinter:
    def output(self, data):
        return f"New Printer: {data}"

# Adapter - converts NewPrinter interface to OldPrinter interface
class PrinterAdapter:
    def __init__(self, new_printer):
        self.new_printer = new_printer
    
    def print_text(self, text):  # Same method as OldPrinter
        return self.new_printer.output(text)

# Usage
old = OldPrinter()
print(old.print_text("Hello"))  # Old Printer: Hello

new = NewPrinter()
# print(new.print_text("Hello"))  # ERROR - NewPrinter doesn't have print_text()

adapter = PrinterAdapter(new)
print(adapter.print_text("Hello"))  # New Printer: Hello ✅