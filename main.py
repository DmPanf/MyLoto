from games import Game
info = """
    Варианты игры:
    0    компьютер <-> компьютер
    1    человек <-> компьютер
    2    человек <-> человек
    3-7  От 3 и до 7 человек (между собой)
"""

if __name__ == '__main__':
    print(f'\n{info}')
    try:
        gamers_count = int(input(f'\n💠 Для выбора игры выбрать число от 0 до 7: '))
        if gamers_count not in range(0,8):
            raise ValueError('⛔️ Ошибка выбора игры!')
        lotto_game = Game(gamers_count)
    except ValueError as error:
        print(error)
        

    while True:
        status, result = lotto_game.play_round() # Возвращается False (мгновенный проигрыш) или True (выигрыш) + номер Игрока
        if result != -1:  # для продолжения игры возвращается -1, иначе индекс победившего игрока (0=Bot)
            w = '〰️' * 16
            if gamers_count > 0:
                user = '🤖 RO-Bot-1 !' if result == 0 else f'Игрок {result} {Game.user_icons[result]}'
            else: # gamers_count == 0
                user = f'🤖 RO-Bot {result}!'
            if status:
                print(f'\n{w}\n🥇🥇🥇 Победил {user} 🎉🎉🎉\n{w}')
            else:
                print(f'\n{w}\n🆘 {user} проиграл ...\n{w}')
            break # останов игры 
