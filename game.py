from card import Card
from tools import clear_screen, random_list, emoji_digits

class Game:
    player_cards = []
    game_barrels = []
    card_colors = ['⬜️', '🟥', '🟨', '🟦', '🟧', '🟪', '🟫', '🟩']
    user_icons = ['🤖 RO-Bot', '🚗', '🚕', '🚙', '🚚', '🚑', '🚒', '🚜']

    def __init__(self, gamers_count):
        gamers_max = 2 if gamers_count < 3 else gamers_count
        for i in range(gamers_max):
            self.player_cards.append(Card(i+1))
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
        if barrel in game_user_card:          # зачеркиваем число в карточке текущего игрока (при наличии)
            game_user_card.cross_num(barrel)
            if game_user_card.closed():       # если карточка текущего игрока полностью закрыта, то победа!
                return True                   # объявляем победителя
        return False                          # продолжаем игру


    def play_round(self):
        # функция выдает комбинацию status и номер user (int)
        # user=-1 с проигравшим или победителем не определились: продолжаем игру
        # если False, то игра прекращается и возвращаем номер проигравшего
        # если True, то игра прекращается и возвращаем номер победителя
        status = False # статус: False=мгновенный проигрыш или True=выигрыш конкретного игрока
        barrel = self.game_barrels.pop()
        emoji_barrel = emoji_digits(barrel)
        print(f'\n🎲 Фишка №: {emoji_barrel}  [{90-len(self.game_barrels)}/{len(self.game_barrels)}]')
        for i, card in enumerate(self.player_cards):
            if gamers_count == 0 or (gamers_count == 1 and i == 0): # Для игр: Бот <-> Бот или Бот <-> Человек
                print(f'\n{self.card_colors[i+1]} Карточка {self.user_icons[0]}-{i+1}\n{card}')
                time.sleep(0.5)                                     # для Бота вопрос "что делать?" опускаем - пауза для наглядности
            else:                                                   #
                print(f'\n{self.card_colors[i+1]} Карточка игрока {i+1} [{self.user_icons[i+1]}]\n{card}')
                status = self.ask_to_cross(card, barrel)            # для игроков запрашиваем, что делать: зачеркнуть [y], иначе - дальше
                if not status:                                      # если игрок ошибся (False), то прекращаем игру 
                    return status, i+1                              # 🆘 возвращаем номер проигравшего игрока (поэтому номер на 1 больше)
            status = self.check_winner_card(card, barrel)           # проверяем остаток незачеркнутых чисел в карточке текущего Бота/игрока
            if status:                                              # если на карточке не осталось чисел, то - окончание игры
                return status, i+1                                  # ✅ при заполнненой карточке объявляем победителя
        
        time.sleep(0.2)
        clear_screen()
        return status, -1                                          # [-1] с проигравшим или победителем не определились: продолжаем игру
