from random import randint as rnd
import os

def clear_screen():
    # Проверка: Operating System == Mac & Linux || Windows
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # Иначе: Operating System = Windows (os.name = nt)
        _ = os.system('cls')
        
"""
# Вариант для Google Colab
from IPython.display import clear_output
def clear_screen():
    clear_output()
"""

def random_list(nums):
    r_list = []
    while len(r_list) < nums:
        rnd_num = rnd(1, 90)
        if rnd_num not in r_list:
            r_list.append(rnd_num)
    return r_list


def emoji_digits(num, emoji='⬜️'): # Функция замены чисел значками emoji
    digits = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
    if num < 10:
        emoji_digits = f'{emoji}{str(digits[num])}' # f'⬜️{str(digits[num])}'
    else:
        digit1 = int(str(num)[0])
        digit2 = int(str(num)[1])
        emoji_digits = f'{str(digits[digit1])}{str(digits[digit2])}'
    return emoji_digits
