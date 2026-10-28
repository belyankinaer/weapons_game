from .weapon import Weapon


class MagicStaff(Weapon):
    def __init__(self, name: str = "Магический посох", damage: int = 35, mana_cost: int = 10):
        super().__init__(name, damage)
        self._mana_cost = mana_cost

    def attack(self) -> str:
        return (
            f"{self._name}: совершает удар "
            f"(-{self._mana_cost} маны), нанося {self._damage} урона!"
        )
