from .bow import Bow
from .character import Character
from .magic_staff import MagicStaff
from .sword import Sword

if __name__ == "__main__":
    hero = Character("Артур")

    weapons = [Sword(), Bow(), MagicStaff("Посох Огня")]

    for weapon in weapons:
        hero.equip(weapon)
        print(hero.attack())
        print("-" * 50)
