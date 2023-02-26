from random import randint as rnd

#from tools import generate_unique_numbers
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
