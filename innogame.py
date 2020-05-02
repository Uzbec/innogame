import random

quest = input("Готовы начать игру?")
counter = 0
guesses = 0
rnd = random.randint(1, 10)
rnd2 = random.randint(1, 10)
rnd3 = random.randint(1, 10)
while counter < 3:
    if "yes" in quest:
        prompt = int(input("Выберите число от 1 до 10"))
        counter += 1
        if prompt == rnd or prompt == rnd2 or prompt == rnd3:
            print("Вы попали")
            guesses += 1
    else:
        break

if guesses == 3:
    print("Вы победили!")
else:
    print("Повезет в следуюший")
