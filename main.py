from game import Game
from player import Player

if __name__ == '__main__':
    # Выводим меню выбора режима игры
    print("Выберите режим игры:")
    print("1. Компьютер-человек")
    print("2. Человек-человек")
    print("3. Компьютер-компьютер")

    # Запрашиваем у пользователя номер выбранного режима
    mode = int(input("Введите номер выбранного режима: "))

    # Создаем объекты класса Player
    if mode == '1':
        player1 = Player('Computer')
        player2 = Player(input('Введите имя игрока: '))
    elif mode == '2':
        player1 = Player(input('Введите имя первого игрока: '))
        player2 = Player(input('Введите имя второго игрока: '))
    else:
        player1 = Player('Computer 1')
        player2 = Player('Computer 2')

    # Создаем объект игры с выбранным режимом и игроками
    game = Game(player1, player2, mode)

    # Запускаем игру
    game.play()

