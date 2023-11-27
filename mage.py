import random
from character import Character
from dice import Dice


class Mage(Character):
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, dice: Dice):
        super().__init__(name, max_hp, attack, defense, dice)
        self._potions = 3
        

    def _apply_critical_strike(self):
        # Spell with a chance to cause burning effect
        if random.random() < 0.7:  # 70% chance of burning effect
            base_damages = random.randint(5, 9)  # Random burning damage between 5 and 9
            print(f"🔥 Fireball! {base_damages} burning damages")
            return base_damages
        else:
            print("🔥 Fireball Cast, No Burning Effect!")
            return 0

    def _apply_potion(self):
        # Attaque avec l'utilisation d'une potion
        if self._potions > 0:
            self._potions -= 1
            potion_bonus = random.randint(5, 10)
    
            print(f"🧪 Used potion! +{potion_bonus} damages")
            return potion_bonus

        else:
            print("🧪 Out of potions! Normal Attack")
            return 0
        
    
    def _apply_heal(self):
        # Attaque avec l'utilisation d'une shield
        if self._potions > 0:
            self._potions -= 1
            heal_bonus = random.randint(5, 10)  # Valeur aléatoire de bonus de shield entre 5 et 10
            print(f"🧪 Used Heal! +{heal_bonus} HP")
            print(f"🧪 {self._potions} potions left")
            self.heal(heal_bonus)
            print(f"🧪 {self.show_healthbar()}")
            

    def _apply_shield(self):
        # Attaque avec l'utilisation d'une shield
        if self._shields > 0:
            self._shields -= 1
            shield_bonus = random.randint(5, 10)  # Valeur aléatoire de bonus de shield entre 5 et 10
            print(f"🧪 Used shield! +{shield_bonus} damages")
            return shield_bonus
        else:
            print("🧪 Out of shields! Normal Attack")
            return 0

    def compute_damages(self, roll, target: Character, attack_type):
        base_damages = self._attack_value + roll
        if attack_type == 1:
            print(f"🔪 Basic Attack: {base_damages} damages ({self._attack_value} damages + {roll} roll)\n")
        elif attack_type == 2:
            base_damages = self._apply_critical_strike()
        elif attack_type == 3:
            self._apply_heal()
            return 0
        return base_damages

# ...