from character import Character, Mage
from dice import Dice
from rich.console import Console
from thief import Thief
from warrior import Warrior
console = Console(width=100)

class Game:
    def __init__(self):
        self._player1 = None
        self._player2 = None

    def choose_character(self):
        console.print("1. Warrior", style="red", justify="center")
        console.print("2. Mage", style="blue", justify="center")
        console.print("3. Thief", style="green" , justify="center")

        choice = input("Enter the number of your choice: ")
        while choice not in ["1", "2", "3"]:
            console.clear()
            console.print("Invalid choice. .")
            console.print("1. Warrior", style="red", justify="center")
            console.print("2. Mage", style="blue", justify="center")
            console.print("3. Thief", style="green" , justify="center")
            choice = input("Enter the number of your choice: ")

        name = input("Enter your character's name: ")
        console.clear()

        if choice == "1":
            return Warrior(name, 20, 8, 3, Dice(6))
        elif choice == "2":
            return Mage(name, 20, 8, 3, Dice(6))
        elif choice == "3":
            return Thief(name, 20, 8, 3, Dice(6))

    def initialize_players(self):
        console.print("Player 1, choose your character.", style="bold red", justify="center")
        print("\n")
        self._player1 = self.choose_character()

        console.print("Player 2, choose your character.", style="bold blue", justify="center")
        self._player2 = self.choose_character()

    def display_status(self):
        input("Press Enter to continue. .")
        console.clear()
        console.print("Current Status", style="bold", justify="center")
        console.print("---------------", style="bold", justify="center")
        console.print(f"{self._player1.get_name()}:")
        console.print(self._player1.show_healthbar())
        console.print("\n")
        console.print(f"{self._player2.get_name()}:")
        console.print(self._player2.show_healthbar())

    def choose_attack(self, player: Character):
        console.print(f"{player.get_name()}'s turn.", style="bold", justify="center")
        console.print("1. Basic Attack")
        console.print("2. Critical Strike (with risk)")
        console.print("3. Use Potion")

        choice = input("Enter the number of your choice: ")
        if choice == "3" and player._get_potions() == 0:
            console.print("You don't have any potions left!", style="bold red", justify="center")
            return self.choose_attack(player)

        while choice not in ["1", "2", "3"]:
            console.clear()
            console.print("Invalid choice. .")
            console.print(f"{player.get_name()}'s turn.", style="bold", justify="center")
            console.print("1. Basic Attack")
            console.print("2. Critical Strike (with risk)")
            console.print("3. Use Potion")
            choice = input("Enter the number of your choice: ")

        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        elif choice == "3":
            return 3

    def run_turn(self):        
        # Player 1's turn
        attack_choice_p1 = self.choose_attack(self._player1)
        print("\n")
        self._player1.attack(self._player2, attack_choice_p1)
        print("\n")
        if not self._player2.is_alive():
            print(f"{self._player1.get_name()} wins!")
            return

        # Player 2's turn
        attack_choice_p2 = self.choose_attack(self._player2)
        self._player2.attack(self._player1, attack_choice_p2)
        if not self._player1.is_alive():
            print(f"{self._player2.get_name()} wins!")
            return

    def run_game(self):
        console.clear()
        console.print("Welcome to the game!", style="bold red underline", justify="center")
        print("\n")
        self.initialize_players()

        while self._player1.is_alive() and self._player2.is_alive():
            self.display_status()
            self.run_turn()

if __name__ == "__main__":
    game = Game()
    game.run_game()