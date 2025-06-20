# Вывод поля
def show_field(field):
    print("  a b c")
    for i, row in enumerate(field):
        print(i, "|".join(row))
        if i < 2:
            print("  -----")

# Ход 
def move(field, y, x, sign):
    if 0 <= y <= 2 and ord("a") <= ord(x) <= ord("c") and field[y][ord(x) - ord("a")] == " ":
        field[y][ord(x) - ord("a")] = sign
    else:
        return False

# Проверка победы
def check_win(field):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2]!= " ":
            return True
        if field[0][i] == field[1][i] == field[2][i]!= " ":
            return True
        if field[0][0] == field[1][1] == field[2][2]!= " ":
            return True
        if field[0][2] == field[1][1] == field[2][0]!= " ":
            return True
    

# Инициализация поля
field = [[" " for _ in range(3)] for _ in range(3)]
# Счётчики
counter = 0
player = 0
print("Добро пожаловать в игру Крестики-Нолики")

# Игровой цикл
while True:
    show_field(field)
    
    if counter % 2 == 0:
        sign = "x"
        player = 1
    else: 
        sign = "o"
        player = 2
    
    print(f"\nХод игрока {player}")
    print('Введите координаты в формате "2 a":')
    y, x = input().split()
    y = int(y)
    
    print()
    
    if move(field, y, x, sign) == False:
        print("Координаты некорректны. Повторите ввод.")
        continue
    counter += 1
    
    if check_win(field) == True:
        show_field(field)
        print(f"\nИгрок {player} выиграл!")
        break