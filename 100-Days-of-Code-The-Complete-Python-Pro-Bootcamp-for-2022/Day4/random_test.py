#A fájlnév ne legyen azonos a beépített függvény nevével, mert az konfliktust okozhat.
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.my_favorite_number)
