from hw9field import Field


class Phone(Field):
    """Представлення поля для зберігання номера телефону, успадковане від класу Field."""

    def __init__(self, number):
        """Ініціалізування поля Phone номером телефону."""
        self.value = self.validate_number(number)

    def validate_number(self, number):
        """Перевірка номеру телефону."""

        if len(number) != 10:
            raise ValueError("Номер телефону має містити 10 цифр.")

        if not number.isdigit():
            raise ValueError("Номер телефону повинен містити тільки цифри.")

        return number