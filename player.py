class Player:
    def __init__(self, name, is_computer=False):
        self.name = name
        self.is_computer = is_computer
        self.card = None

    def select_card(self, card):
        self.card = card

    def show_card(self):
        if self.card:
            print(f"\nКарточка игрока {self.name}:")
            self.card.show()
        else:
            print("Карточка не выбрана!")

    def select_number(self, barrel):
        if self.card:
            if self.card.contains(barrel):
                self.card.cross_out(barrel)
                print(f"\nИгрок {self.name} вычеркивает номер {barrel}!")
                return True
            else:
                print(f"\nИгрок {self.name} не нашел номер {barrel} на своей карточке.")
        else:
            print("Карточка не выбрана!")
        return False
