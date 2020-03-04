"""
    Main file of BlackJack game
"""

from blackjack.game import Game
from blackjack.cli import get_answer
from blackjack.player import Player, AiPlayer

def main_game():
    players = [Player('Bob', 500), AiPlayer('Sam', 500)]
    dealer = AiPlayer('Dealer', 5000)
    game = Game(players, dealer)

    print('\nWelcome!\n')
    game.game_loop()
    print('\nThanks for playing!')


if __name__ == '__main__':
    main_game()
