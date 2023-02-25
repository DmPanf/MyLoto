import random
from card import Card


class Game:
    def __init__(self, player1, player2, mode):
        self.players = [player1, player2]
        self.mode = mode
        self.deck = self._create_deck()
        self.winner = None

    def _create_deck(self):
        deck = []
        for i in range(1, 91):
            deck.append(i)
        random.shuffle(deck)
        return deck

    def play(self):
        for i in range(1, 91):
            print(f'\nХод номер {i}\n')
            number = self.deck.pop()
            print(f'Выпало число {number}!\n')
            for player in self.players:
                print(f'Ход игрока {player.name}!\n')
                if self.mode == '1' and player.is_computer:
                    print(f'Карточка игрока {player.name}:')
                    player.card.display()
                    input('Нажмите Enter, чтобы продолжить...')
                elif self.mode == '2' or not player.is_computer:
                    print(f'Карточка игрока {player.name}:')
                    player.card.display()
                    while True:
                        try:
                            answer = input(f'{player.name}, зачеркнуть число {number}? (y/n)\n')
                            if answer.lower() == 'y':
                                player.card.cross_out(number)
                                break
                            elif answer.lower() == 'n':
                                break
                            else:
                                print('Некорректный ввод! Введите "y" или "n"')
                        except KeyboardInterrupt:
                            print('\nИгра остановлена пользователем!')
                            exit()

                if player.card.is_winner():
                    self.winner = player
                    break

            if self.winner is not None:
                break

        if self.winner is None:
            print('\nНичья!')
        else:
            print(f'\nПобедил игрок {self.winner.name}!')

