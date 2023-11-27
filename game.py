from character import Character
from dice import Dice
from rich.console import Console, Theme
from thief import Thief
from warrior import Warrior
from mage import Mage
from time import sleep

theme = Theme({
    "info": "bold green",
    "warning": "bold yellow",
    "danger": "bold red",
})

console = Console(width=100, theme=theme, highlight=False)

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
            # Guerrier
            return Warrior(name, max_hp=60, attack=8, defense=4, dice=Dice(6))
        elif choice == "2":
            # Mage
            return Mage(name, max_hp=40, attack=12, defense=3, dice=Dice(6))
        elif choice == "3":
            # Voleur
            return Thief(name, max_hp=45, attack=10, defense=5, dice=Dice(6))


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
        self.show_healthbar(self._player1)
        console.print("\n")
        console.print(f"{self._player2.get_name()}:")
        self.show_healthbar(self._player2)

    def show_healthbar(self, player: Character):
        missing_hp = player._max_hp - player._current_hp
        console.print(f"[{' ' * player._current_hp}]", end="\r")
        for i in range(1, player._current_hp + 1):
            healthbar = f"[{'♥' * i}{'♡' * missing_hp}] {i}/{player._max_hp}hp"
            console.print(healthbar, style="bold red"  ,end="\r")
            sleep(0.025)
        console.print("\n")
        console.print(f" ({player.get_potions()} potions)", style="green")

    def choose_attack(self, player: Character):
        console.print(f"{player.get_name()}'s turn.", style="bold", justify="center")
        console.print("[bold bright_red]1.[/] Basic Attack", style="blue")
        console.print("[bold bright_red]2.[/] Critical Strike (with risk)", style="orange1")
        console.print("[bold bright_red]3.[/] Use Potion \n", style="green")

        choice = input("Enter the number of your choice: ")
        if choice == "3" and player.get_potions() == 0:
            console.print("You don't have any potions left!", style="bold red", justify="center")
            return self.choose_attack(player)

        while choice not in ["1", "2", "3"]:
            console.clear()
            console.print("Invalid choice. .\n", style="bold red", justify="center")
            console.print(f"{player.get_name()}'s turn.", style="bold", justify="center")
            console.print("[bold bright_red]1.[/] Basic Attack", style="blue")
            console.print("[bold bright_red]2.[/] Critical Strike (with risk)", style="orange1")
            console.print("[bold bright_red]3.[/] Use Potion \n", style="green")
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
        if (attack_choice_p1 == 3):
            self.show_healthbar(self._player1)
        else:
            self.show_healthbar(self._player2)
        print("\n")
        if not self._player2.is_alive():
            self.display_victory_animation(self._player1.get_name())
            return

        # Player 2's turn
        attack_choice_p2 = self.choose_attack(self._player2)
        self._player2.attack(self._player1, attack_choice_p2)
        if (attack_choice_p2 == 3):
            self.show_healthbar(self._player2)
        else:
            self.show_healthbar(self._player1)
        if not self._player1.is_alive():
            self.display_victory_animation(self._player2.get_name())
            return

    def display_victory_animation(self, player_name):
        console.clear()

        colors = ["green", "yellow", "red", "blue", "magenta"]
        
        # Animation de texte coloré
        for i in range(1, 5):
            for color in ["green", "yellow", "red", "blue"]:
                message = f"[{color}][bold]{player_name}[/bold] a remporté la victoire ![/]"
                console.print(message, style=color, justify="center")
                console.print()
                console.print()
                console.print(f"[info][{colors[i]}]Bravo ![/][/info]", justify="center")
                console.print()
                console.print()
                console.print("[bold]Rejouer : Appuyez sur une touche...[/bold]", style="info", justify="center")
                sleep(0.5)
                
                # Attendre une courte période pour créer l'effet d'animation
                console.show_cursor(False)
                console.clear()
        
        console.show_cursor(True)

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