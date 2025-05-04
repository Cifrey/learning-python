import random

# print(help(random))

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number = random.randint(1, 20) # Saca un número random entre (a, b)
number = random.randint(low, high)
number = random.random() # Esto saca un número random entre 0 y 1, con muchos decimales
option = random.choice(options)
random.shuffle(cards)
print(cards)