import random

from .weapon import Weapon


class Bow(Weapon):
    def __init__(self, name: str = "Лук", damage: int = 18, hit_chance: float = 0.8):
        super().__init__(name, damage)
        self._hit_chance = hit_chance

    def attack(self) -> str:
        current_hit = random.random()

        if current_hit < self._hit_chance:
            return f"{self._name}: натягивает тетиву и попадает в цель, нанося {self._damage} урона!"

        return f"{self._name}: стрела летит мимо — промах!"
