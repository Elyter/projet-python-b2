import random
from character import Character
from dice import Dice 
from character import Thief

class Warrior(Character):
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, dice: Dice):
        super().__init__(name, max_hp, attack, defense, dice)
        self._shields = 3

    def _apply_attack_modifiers(self, base_damages: int, target: Character):
        print (f"🪓 Basic Attack: {base_damages + target.get_defense_value()} damages")

    def _apply_critical_strike(self, base_damages: int):
        if random.random() < 0.3:
            malus = random.randit(1, 5)
            print (f"💔 Critical Strike ! {malus} damages")
            return base_damages - malus 
        else : 
            print ("💔 Critical Strike Failed !")
            return base_damages 
        
    def _apply_shield(self):
        if self._shields > 0:
            self._shields -= 1
            shield_bonus = random.randint(5, 10) 
            print (f"🛡️ Used shield ! + {shield_bonus} defense")
            return shield_bonus 
        else : 
            print (f"🛡️ Out of shields ! Normal Defense")
            return 0 

    def compute_damages(self, roll, target: Character):
        print (f"🪓 Bonus: Axe in your face(+3 attack)")
        base_damages = super().compute_damages(roll, target) + 3 

        damages_after_critical = self._apply_critical_strike(base_damages)

        final_damages = damages_after_critical + self._apply_shield()

        return final_damages

if __name__ == "__main__":
    character1 = Thief("Lisa", 20, 8, 3, Dice(6))
    character2 = Warrior("Salim", 20, 8, 3, Dice(6))
    print(character1)
    print(character2)

    while character1.is_alive() and character2.is_alive():
        character1.attack(character2)
        character2.attack(character1)
