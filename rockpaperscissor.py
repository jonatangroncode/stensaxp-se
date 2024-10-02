import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["sten", "sax", "påse"]
        self.player_choice = None
        self.computer_choice = None

    def get_computer_choice(self):
        """Väljer slumpmässigt ett val för datorn."""
        self.computer_choice = random.choice(self.choices)
        return self.computer_choice

    def get_player_choice(self):
        """Frågar spelaren om deras val."""
        while True:
            choice = input("Välj sten, sax eller påse: ").lower()
            if choice in self.choices:
                self.player_choice = choice
                break
            else:
                print("Ogiltigt val. Försök igen.")

    def determine_winner(self):
        """Avgör vinnaren baserat på spelarens och datorns val."""
        if self.player_choice == self.computer_choice:
            return "Oavgjort!"
        elif (self.player_choice == "sten" and self.computer_choice == "sax") or \
             (self.player_choice == "sax" and self.computer_choice == "påse") or \
             (self.player_choice == "påse" and self.computer_choice == "sten"):
            return "Du vann!"
        else:
            return "Datorn vann!"

def main():
    while True:
        game = RockPaperScissors()
        
        game.get_player_choice()

        computer_choice = game.get_computer_choice()
        print(f"Datorn valde: {computer_choice}")

        result = game.determine_winner()
        print(result)

        play_again = input("Vill du spela igen? (ja/nej): ").lower()
        if play_again != "ja":
            print("Okej kanske en annan gång hejdå")
            break

if __name__ == "__main__":
    main()

