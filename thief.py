import random
from character import Character
from dice import Dice
from character import Warrior

class Thief(Character):
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, dice: Dice):
        super().__init__(name, max_hp, attack, defense, dice)
        self._potions = 3

    def _apply_attack_modifiers(self, base_damages: int, target: Character):
        # Attaque de base avec bonus de défense de la cible
        print(f"🔪 Basic Attack: {base_damages + target.get_defense_value()} damages")

    def _apply_critical_strike(self, base_damages: int):
        # Attaque avec un pourcentage de chance d'avoir un malus
        if random.random() < 0.3:  # 30% de chance d'avoir un malus
            malus = random.randint(1, 5)  # Valeur aléatoire de malus entre 1 et 5
            print(f"💔 Critical Strike! {malus} damages")
            return base_damages - malus
        else:
            print("💔 Critical Strike Failed!")
            return base_damages

    def _apply_potion(self):
        # Attaque avec l'utilisation d'une potion
        if self._potions > 0:
            self._potions -= 1
            potion_bonus = random.randint(5, 10)  # Valeur aléatoire de bonus de potion entre 5 et 10
            print(f"🧪 Used Potion! +{potion_bonus} damages")
            return potion_bonus
        else:
            print("🧪 Out of Potions! Normal Attack")
            return 0

    def compute_damages(self, roll, target: Character):
        print(f"🔪 Bonus: Sneaky Attack (+{target.get_defense_value()} damages)")
        base_damages = super().compute_damages(roll, target) + target.get_defense_value()

        # Appliquer un coup critique avec un malus potentiel
        damages_after_critical = self._apply_critical_strike(base_damages)

        # Appliquer l'utilisation éventuelle d'une potion
        final_damages = damages_after_critical + self._apply_potion()

        return final_damages

# ...

if __name__ == "__main__":
    character1 = Warrior("Salim", 20, 8, 3, Dice(6))
    character2 = Thief("Lisa", 20, 8, 3, Dice(6))
    print(character1)
    print(character2)

    while character1.is_alive() and character2.is_alive():
        character1.attack(character2)
        character2.attack(character1)
