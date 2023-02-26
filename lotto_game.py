from random import randint as rnd
from tools import clear_screen, random_list, emoji_digits
import time


class Card:
    card_rows = 3
    card_cols = 9
    card_nums_in_row = 5
    card_data = None
    card_empty_num = 0
    card_crossed_num = -1
    emj = '⬜️'

    def __init__(self, i_user):
        uniques_num = self.card_nums_in_row * self.card_rows # количество уникальных чисел 5*3=15
        uniques = random_list(uniques_num)
        self.emj = Game.card_colors[i_user]

        self.card_data = [] #  формирование карточки
        for i in range(0, self.card_rows): # перебор 3 рядов (от 0 до 2)
            tmp = sorted(uniques[self.card_nums_in_row * i: self.card_nums_in_row * (i + 1)]) # списки [0:5][5:10][10:15]
            empty_nums_count = self.card_cols - self.card_nums_in_row  # 9-5=4
            for j in range(0, empty_nums_count): # заполняем карточку пробелами (0) на случайных позициях
                index = rnd(0, len(tmp))
                tmp.insert(index, self.card_empty_num)
            self.card_data += tmp   # формируем полную карточку для игры


    def __str__(self):  # Функция заполнения карточки с числами графичискими элементами
        emj0 = '🔲'
        str_line = '〰️' * 26
        result = str_line + '\n'
        for index, num in enumerate(self.card_data):
            if num == self.card_empty_num:      # заполнение пробелов (=0)
                result +=  self.emj * 2     # '⬜️⬜️'
            elif num == self.card_crossed_num:  # вместо зачеркнутых чисел
                result += self.emj + emj0   # '⬜️🔲'
            else:
                result += emoji_digits(num, self.emj)

            if (index + 1) % self.card_cols == 0:  # Перевод строки за последним числом в ряду
                result += '\n'
            else:
                result += self.emj          # '⬜️'
        return result + str_line


    def __contains__(self, item): # метод класса: содержится ли заданный элемент в карточке игрока
        is_contains = item in self.card_data
        return is_contains


    def cross_num(self, num): # функция "зачеркивания" чисел на карточке при совпадении
        for index, item in enumerate(self.card_data):
            if item == num:
                self.card_data[index] = self.card_crossed_num
                return
        raise ValueError(f'❌ На карточке нет числа: {num}')


    def closed(self) -> bool:  # если множества равны, то все ячейки на карточке заполнены, и функция возвращает True
        is_closed = set(self.card_data) == {self.card_empty_num, self.card_crossed_num}
        return is_closed


class Game:
    player_cards = []
    game_barrels = []
    card_colors = ['⬜️', '🟥', '🟨', '🟦', '🟧', '🟪', '🟫', '🟩']
    user_icons = ['🤖 RO-Bot', '🚗', '🚕', '🚙', '🚚', '🚑', '🚒', '🚜']

    def __init__(self, gamers_count):
        gamers_max = 2 if gamers_count < 3 else gamers_count
        for i in range(gamers_max):
            self.player_cards.append(Card(i + 1))
        self.game_barrels = random_list(90)

    def ask_to_cross(self, game_user_card, barrel) -> bool:
        # При выборе "зачеркнуть": если цифры на карточке нет - игрок проигрывает, и игра завершается
        # При выборе "продолжить": если цифра есть на карточке - игрок проигрывает, и игра завершается
        # ... иначе - игра продолжается!
        y_n = input('... зачеркнуть [y] ... нет, продолжить [n]: ').lower().strip()
        if y_n == 'y' and not barrel in game_user_card or y_n != 'y' and barrel in game_user_card:
            return False
        return True

    def check_winner_card(self, game_user_card, barrel):
        if barrel in game_user_card:  # зачеркиваем число в карточке текущего игрока (при наличии)
            game_user_card.cross_num(barrel)
            if game_user_card.closed():  # если карточка текущего игрока полностью закрыта, то победа!
                return True  # объявляем победителя
        return False  # продолжаем игру

    def play_round(self, gamers_count):
        # функция выдает комбинацию status и номер user (int)
        # user=-1 с проигравшим или победителем не определились: продолжаем игру
        # если False, то игра прекращается и возвращаем номер проигравшего
        # если True, то игра прекращается и возвращаем номер победителя
        status = False  # статус: False=мгновенный проигрыш или True=выигрыш конкретного игрока
        barrel = self.game_barrels.pop()
        emoji_barrel = emoji_digits(barrel)
        print(f'\n🎲 Фишка №: {emoji_barrel}  [{90 - len(self.game_barrels)}/{len(self.game_barrels)}]')
        for i, card in enumerate(self.player_cards):
            if gamers_count == 0 or (gamers_count == 1 and i == 0):  # Для игр: Бот <-> Бот или Бот <-> Человек
                print(f'\n{self.card_colors[i + 1]} Карточка {self.user_icons[0]}-{i + 1}\n{card}')
                time.sleep(0.5)  # для Бота вопрос "что делать?" опускаем - пауза для наглядности
            else:  #
                print(f'\n{self.card_colors[i + 1]} Карточка игрока {i + 1} [{self.user_icons[i + 1]}]\n{card}')
                status = self.ask_to_cross(card, barrel)  # для игроков запрашиваем, что делать: зачеркнуть [y], иначе - дальше
                if not status:  # если игрок ошибся (False), то прекращаем игру
                    return status, i + 1  # 🆘 возвращаем номер проигравшего игрока (поэтому номер на 1 больше)
            status = self.check_winner_card(card, barrel)  # проверяем остаток незачеркнутых чисел в карточке текущего Бота/игрока
            if status:  # если на карточке не осталось чисел, то - окончание игры
                return status, i + 1  # ✅ при заполнненой карточке объявляем победителя

        time.sleep(0.2)
        clear_screen()
        return status, -1  # [-1] с проигравшим или победителем не определились: продолжаем игру
