"""
    Main file of BlackJack game
"""

from blackjack.game import Game
from blackjack.cli import get_answer
from blackjack.player import Player, Dealer

def main_game():
    players = [Player('Bob', 500)]
    dealer = Dealer('Dealer', 5000)
    game = Game(players, dealer)
    while True:
        print('\nWelcome!\n')
        game.start_game()

        print('\nGame finished')

        for player in players:
            if player.budget < 2:
                print(f'Out of budget, {player.name}. Bye!')
                players.remove(player)

        if not players:
            break

        print('\nReplay?')
        if get_answer() == 'n':
            break

    print('\nThanks for playing!')


if __name__ == '__main__':
    main_game()
