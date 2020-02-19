"""
    Main file of BlackJack game
"""

from blackjack.game import Game
from blackjack.cli import get_answer

def main_game():
    replay = True
    while replay:
        print('\nWelcome!\n')
        game = Game()
        game.start_game()

        print('\nGame finished')
        print('\nReplay?')
        replay = get_answer() == 'y'

    print('\nBye')


if __name__ == '__main__':
    main_game()
