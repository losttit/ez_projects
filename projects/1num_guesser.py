from random import randint

def is_valid(num, r_g):
    if num.isdigit() and r_g.isdigit() and 1 <= int(num) <= int(r_g):
        return True
    else:
        return False

print("Добро пожаловать в числовую угадайку")
r_g = input("Введите правую гранимцу случайного числа:\n")
r_num = randint(1, int(r_g))
count = 0
while True:
    count += 1
    print(f"Введите число от 1 до {r_g}")
    num = input()
    if is_valid(num, r_g):
        num = int(num)
        if num < r_num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif num > r_num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif num == r_num:
            print(f'Вы угадали c {count} попытки, поздравляем!\nЕсли хотите ещё, нажмите "e", если хотите выйти - "q"')
            key = input()
            if key == "e":
                print("Начинаем сначала")
                count = 0
                r_g = input("Введите правую гранимцу случайного числа:\n")
                r_num = randint(1, int(r_g))
            elif key == "q":
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break
    else:
        print("А может быть все-таки введем целое число от 1 до 100?")