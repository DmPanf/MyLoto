import random

class Card:
    def __init__(self):
        self.numbers = [[0] * 9 for i in range(3)]
        self.numbers[1][0] = -1  # Разделитель в середине карточки

    def generate(self):
        nums = random.sample(range(1, 91), 15)
        nums.sort()

        for i, num in enumerate(nums):
            row = i // 5
            col = nums[i] % 10 - 1
            if col == -1:
                col = 8
            self.numbers[row][col] = num

    def show(self):
        for row in self.numbers:
            line = "|".join([str(num).center(2) if num > 0 else "  " for num in row])
            print(line)

    def contains(self, num):
        for row in self.numbers:
            if num in row:
                return True
        return False

    def cross_out(self, num):
        for i, row in enumerate(self.numbers):
            if num in row:
                j = row.index(num)
                self.numbers[i][j] = -1
