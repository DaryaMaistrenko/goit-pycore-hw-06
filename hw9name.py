from hw9field import Field


class Name(Field):
    """Представлення поля для зберігання імені, успадковане від класу Field."""

    def __init__(self, name):
        """Ініціалізування поля Name ім'ям."""
        self.value = name