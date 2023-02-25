import random


class Card:
    def __init__(self):
        self.card = self.generate_card()

    def generate_card(self):
        card = []
        card.append(random.sample(range(1, 91), 5))
        card.append(random.sample(range(1, 91), 5))
        card.append(random.sample(range(1, 91), 5))
        return card

    def check_number(self, number):
        for i in range(len(self.card)):
            if number in self.card[i]:
                self.card[i][self.card[i].index(number)] = '-'

        self.print_card()

        for i in range(len(self.card)):
            if '-' not in self.card[i]:
                return True

        return False

    def print_card(self):
        print('-' * 15)
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                if self.card[i][j] == '-':
                    print('  ', end='')
                elif self.card[i][j] < 10:
                    print(f' {self.card[i][j]}', end='')
                else:
                    print(self.card[i][j], end='')
                if j != 4:
                    print(' ', end='')
            print()
        print('-' * 15)


class Lotto:
    def __init__(self, mode, players):
        self.mode = mode
        self.players = players
        self.cards = []
        self.numbers = random.sample(range(1, 91), 90)
        self.winners = []

    def play(self):
        print('Добро пожаловать в Лото!')
        for i in range(self.players):
            if self.mode == '1':
                if i == 0:
                    self.cards.append(Card())
                    print('Карточка игрока 1:')
                    self.cards[-1].print_card()
                else:
                    self.cards.append(Card())
                    print('Карточка компьютера:')
            elif self.mode == '2':
                self.cards.append(Card())
                print(f'Карточка игрока {i+1}:')
                self.cards[-1].print_card()
            else:
                self.cards.append(Card())
                print(f'Карточка компьютера {i+1}:')

        while True:
            input_str = input('Нажмите Enter, чтобы продолжить или Q, чтобы закончить игру: ').lower()
            if input_str == 'q':
                break

            number = self.numbers.pop()
            print(f'Новый бочонок: {number} (осталось {len(self.numbers)} бочонков)')
            for i in range(len(self.cards)):
                if self.cards[i].check_number(number):
                    if self.mode == '1' and i == 1:
                        print('Выиграл компьютер!')
                    elif self.mode == '2':
                        print(f'Выиграл игрок {i+1}!')
                    else:
                        print(f'Выиграл компьютер {i+1}!')

                    self.winners.append(i+1)
                    return

        print('Игра окончена!')
        if self.winners:
            print('Победители:')
            for winner in set(self.winners):
                print(f'Игрок {winner}')
        else:
            print('Победителей нет.')
