from __future__ import annotations
print("\n")

from dice import Dice

from rich import print

class MessageManager():
    pass

class Character:
    
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, dice: Dice):
        self._name = name
        self._max_hp = max_hp
        self._current_hp = max_hp
        self._attack_value = attack
        self._defense_value = defense
        self._dice = dice

    def __str__(self):
        return f"""{self._name} the Character enter the arena with :
    ■ attack: {self._attack_value} 
    ■ defense: {self._defense_value}"""
        
    def get_defense_value(self):
        return self._defense_value
        
    def get_name(self):
        return self._name
        
    def is_alive(self):
        return self._current_hp > 0       

    def regenerate(self):
        self._current_hp = self._max_hp

    def heal(self, amount):
        self._current_hp += amount
        if self._current_hp > self._max_hp:
            self._current_hp = self._max_hp

    def decrease_health(self, amount):
        self._current_hp -= amount
        if self._current_hp < 0:
            self._current_hp = 0
        print(f"{self._name} : {self.show_healthbar()}\n")

    def attack(self, target: Character, attack_type):
        if not self.is_alive():
            return
        roll = self._dice.roll()
        damages = self.compute_damages(roll, target, attack_type)
        if damages > 0:
            target.defense(damages, self)
    
    def compute_defense(self, damages, roll, attacker):
        return damages - self._defense_value - roll
    
    def defense(self, damages, attacker: Character):
        roll = self._dice.roll()
        wounds = self.compute_defense(damages, roll, attacker)
        if wounds < 0:
            wounds = 0
        print(f"🛡️ {self._name} take {wounds} wounds from {attacker.get_name()} (damages: {damages} - defense: {self._defense_value} - roll: {roll})\n")
        self.decrease_health(wounds)

class Mage(Character):
    def compute_defense(self, damages, roll, attacker: Character):
        print("🧙 Bonus: Magic armor (-3 damages)")
        return super().compute_defense(damages, roll, attacker) - 3

if __name__ == "__main__":
    character1 = Warrior("Salim", 20, 8, 3, Dice(6))
    character2 = Thief("Lisa", 20, 8, 3, Dice(6))
    print(character1)
    print(character2)
    
    while (character1.is_alive() and character2.is_alive()):
        character1.attack(character2)
        character2.attack(character1)
