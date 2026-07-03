# Real object - expensive to create
class RealDatabase:
    def __init__(self):
        print("Creating expensive database connection...")
    
    def fetch_data(self, query):
        return f"Data from query: {query}"

# Proxy - controls access to RealDatabase
class DatabaseProxy:
    def __init__(self):
        self.real_db = None  # Not created yet (lazy loading)
    
    def fetch_data(self, query):
        # Check permission first
        if not self.is_authorized():
            return "Access Denied!"
        
        # Create real object only when needed
        if self.real_db is None:
            self.real_db = RealDatabase()
        
        return self.real_db.fetch_data(query)
    
    def is_authorized(self):
        return True  # Can add permission checks here

# Usage
proxy = DatabaseProxy()
print(proxy.fetch_data("SELECT * FROM users"))  # Creates DB only now
print(proxy.fetch_data("SELECT * FROM orders"))  # Reuses existing DB