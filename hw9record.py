from hw9phone import Phone
from hw9name import Name


class Record:
    """Представлення запису контакту, що містить ім’я та список телефонних номерів."""

    def __init__(self, name):
        """Ініціалізування запису за допомогою імені та порожнього списку телефонів."""
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        """Повертання рядкового представлення запису."""

        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, number: str):
        """Додавання номер телефону до запису."""
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        """Видалення номера телефону із запису."""

        self.phones = list(filter(lambda phone: phone == number, self.phones))

    def edit_phone(self, old_number, new_number):
        """Відредагування номера телефону в записі."""

        self.phones = list(
            map(
                lambda phone: Phone(new_number) if phone.value == old_number else phone,
                self.phones,
            )
        )

    def find_phone(self, number):
        """Знаходження у записі номер телефону."""

        for phone in self.phones:
            if phone.value == number:
                return phone