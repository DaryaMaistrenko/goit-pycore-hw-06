from collections import UserDict


class AddressBook(UserDict):
    """Створення нової адресної книги."""

    def add_record(self, record):
        """Створення запису для ...."""
        if record.name.value in self.data:
            raise KeyError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        """Пошук імені."""
        record = self.data.get(name, None)
        if record is None:
            raise KeyError(f"Record with name '{name}' not found.")
        return record

    def delete(self, name):
        """Видалення імені."""
        if name not in self.data:
            raise KeyError(f"Record with name '{name}' not found.")
        del self.data[name]