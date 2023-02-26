
class Game:
    player_cards = []
    game_barrels = []
    card_colors = ['⬜️', '🟥', '🟨', '🟦', '🟧', '🟪', '🟫', '🟩']
    user_icons = ['🤖 Bot', '🚗', '🚕', '🚙', '🚚', '🚑', '🚒', '🚜']

    def __init__(self, gamers_count):
        for i in range(gamers_count):
            self.player_cards.append(Card())
        self.game_barrels = random_list(90)

    def play_round(self) -> int:
        barrel = self.game_barrels.pop()
        emoji_barrel = emoji_digits(barrel)
        clear_screen()
        for i, card in enumerate(self.player_cards):
            print(f'\n{self.card_colors[i+1]} Карточка игрока {i+1}: {self.user_icons[i+1]}\n{card}')
        
        print(f'\n🎲 Фишка №: {emoji_barrel}  [{90-len(self.game_barrels)}/{len(self.game_barrels)}]')
        
        return 1
