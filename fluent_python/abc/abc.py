from abc import ABC, abstractmethod, abstractclassmethod
from collections.abc import MutableSequence

# Example 1: ABC with class methods
class DatabaseConnector(ABC):
    @abstractclassmethod
    def get_connection(cls) -> str:
        """Get database connection."""
        pass

    @abstractmethod
    def query(self, sql: str) -> list:
        """Execute a query."""
        pass

class PostgresConnector(DatabaseConnector):
    @classmethod
    def get_connection(cls) -> str:
        return "postgres://localhost:5432"
    
    def query(self, sql: str) -> list:
        return [f"Executing {sql} on Postgres"]

# Example 2: ABC MutableSequence
class OrderedList(MutableSequence):
    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
        self._items.sort()
    
    def __delitem__(self, index):
        del self._items[index]
    
    def insert(self, index, value):
        self._items.insert(index, value)
        self._items.sort()

# Usage examples
if __name__ == "__main__":
    # Database example
    db = PostgresConnector()
    print(db.get_connection())
    print(db.query("SELECT * FROM users"))

    # OrderedList example
    ordered = OrderedList()
    ordered.extend([3, 1, 4, 1, 5])
    print(ordered._items)  # Will be sorted automatically