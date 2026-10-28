from .weapon import Weapon


class Sword(Weapon):
    def __init__(self, name: str = "Меч", damage: int = 25):
        super().__init__(name, damage)

    def attack(self) -> str:
        return f"{self._name}: наносит {self._damage} урона!"
