import random
from typing import final
import itertools

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_added = []
symbols_added = []
numbers_added = []

for i in range(0, nr_letters):
    letters_added.append(letters[random.randint(0, len(letters)-1)])

for i in range(0, nr_symbols):
    symbols_added.append(symbols[random.randint(0, len(symbols)-1)])

for i in range(0, nr_numbers):
    numbers_added.append(numbers[random.randint(0, len(numbers)-1)])

letters_pass = ""
symbols_pass = ""
numbers_pass = ""

for i in letters_added:
    letters_pass += i

for i in symbols_added:
    symbols_pass += i

for i in numbers_added:
    numbers_pass += i

x = []

for i in range(0, len(letters_added)):
    x.append(letters_added[i])

y = []

for i in range(0, len(symbols_added)):
    y.append(symbols_added[i])

z = []

for i in range(0, len(numbers_added)):
    z.append(numbers_added[i])

new_list = x + y + z
easy_solution = ""

for i in new_list:
    easy_solution += i

shuffled_list = sorted(new_list, key=lambda p: random.random())

final_pass = ""

for i in shuffled_list:
    final_pass += i

print(final_pass)