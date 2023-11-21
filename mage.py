import random
from character import Character
from dice import Dice
from character import Mage


class Mage(Character):
    def __init__(self, name: str, max_hp: int, attack: int, defense: int, dice: Dice):
        super().__init__(name, max_hp, attack, defense, dice)
        self._mana = 10

    def _apply_attack_modifiers(self, base_damages: int, target: Character):
        # Basic spell with bonus based on target's defense
        print(f"🔮 Basic Spell: {base_damages + target.get_defense_value()} damages")

    def _apply_fireball(self):
        # Spell with a chance to cause burning effect
        if random.random() < 0.2:  # 20% chance of burning effect
            burning_damage = random.randint(3, 8)  # Random burning damage between 3 and 8
            print(f"🔥 Fireball! {burning_damage} burning damages")
            return burning_damage
        else:
            print("🔥 Fireball Cast, No Burning Effect!")
            return 0

    def _apply_mana_shield(self):
        # Spell to create a mana shield for defense
        shield_value = random.randint(5, 10)  # Random shield value between 5 and 10
        print(f"🛡️ Mana Shield! +{shield_value} defense")
        return shield_value

    def _consume_mana(self):
        # Consume mana for spell casting
        if self._mana >= 3:
            self._mana -= 3
            print("🔵 Mana Consumed: -3 mana")
            return True
        else:
            print("🔵 Out of Mana! Basic Spell Used")
            return False

    def compute_damages(self, roll, target: Character):
        print(f"🔮 Bonus: Arcane Power (+{target.get_defense_value()} damages)")
        base_damages = super().compute_damages(roll, target) + target.get_defense_value()

        # Apply Fireball spell with potential burning effect
        fireball_damages = self._apply_fireball()

        # Consume mana and apply Mana Shield for defense
        if self._consume_mana():
            mana_shield_value = self._apply_mana_shield()
            base_damages += mana_shield_value

        return base_damages + fireball_damages

# ...