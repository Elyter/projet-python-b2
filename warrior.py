import random
from character import Character
from dice import Dice

class Warrior(Character):
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, dice: Dice):
        super().__init__(name, max_hp, attack, defense, dice)
        self._potions = 3

    def _apply_critical_strike(self, base_damages: int, roll):
        # Attaque avec un pourcentage de chance d'avoir un malus
        if random.random() < 0.6:  # 30% de chance d'avoir un malus
            bonus = random.randint(1, 5)  # Valeur aléatoire de malus entre 1 et 5
            print(f"💔 Critical Strike! {base_damages + bonus} Damages (+{bonus} bonus damages + {self._attack_value} damages + {roll} roll)\n")
            return base_damages + bonus
        else:
            malus = random.randint(1, 5)  # Valeur aléatoire de malus entre 1 et 5
            print(f"💔 Critical Strike Failed! {base_damages - malus} Damages (-{malus} damages + {self._attack_value} damages + {roll} roll)\n")
            return base_damages - malus

    def _apply_heal(self):
        # Attaque avec l'utilisation d'une shield
        if self._potions > 0:
            self._potions -= 1
            heal_bonus = random.randint(5, 10)  # Valeur aléatoire de bonus de shield entre 5 et 10
            print(f"🧪 Used Heal! +{heal_bonus} HP")
            print(f"🧪 {self._potions} potions left")
            self.heal(heal_bonus)
            
    def compute_damages(self, roll, target: Character, attack_type):
        base_damages = self._attack_value + roll
        if attack_type == 1:
            print(f"🔪 Basic Attack: {base_damages} damages ({self._attack_value} damages + {roll} roll)\n")
        elif attack_type == 2:
            base_damages = self._apply_critical_strike(base_damages, roll)
        elif attack_type == 3:
            self._apply_heal()
            return 0
        return base_damages