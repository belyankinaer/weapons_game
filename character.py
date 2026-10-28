from typing import Optional

from .weapon import Weapon


class Character:
    def __init__(self, name: str, weapon: Optional[Weapon] = None):
        self._name = name
        self._weapon = weapon

    def equip(self, weapon: Weapon) -> None:
        self._weapon = weapon

        weapon_name = weapon.get_name
        print(f"{self._name} экипировал: {weapon_name}")

    def attack(self) -> str:
        if self._weapon is None:
            return f"{self._name} безоружен и не может атаковать!"

        return f"{self._name} -> {self._weapon.attack()}"
