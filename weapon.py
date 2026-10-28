from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self, name: str, damage: int):
        self._name = name
        self._damage = damage

    @property
    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def attack(self) -> str:
        """Атаковать. Возвращает описание атаки."""
        pass
