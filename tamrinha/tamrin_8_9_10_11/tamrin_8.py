import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

deck = [[suit, rank] for suit in suits for rank in ranks]

print("دسته ورق قبل از برزدن:")
print(deck[:5]) 
print("...\n")

# برزدن ورق‌ها
random.shuffle(deck)

print("دسته ورق بعد از برزدن:")
print(deck[:5])  
print("...")
