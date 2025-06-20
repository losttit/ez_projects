def convert_number():
    number_str = input("Введите число: ").strip().upper()
    source_base = int(input("Исходная система (2, 8, 10, 16): "))
    target_base = int(input("Целевая система (2, 8, 10, 16): "))
    
    try:
        decimal_num = int(number_str, base=source_base)
    except ValueError:
        print("Ошибка: Некорректное число для указанной системы счисления!")
        return

    if target_base == 2:
        result = bin(decimal_num)[2:]
    elif target_base == 8:
        result = oct(decimal_num)[2:]
    elif target_base == 10:
        result = decimal_num
    elif target_base == 16:
        result = hex(decimal_num)[2:].upper()
    else:
        print("Ошибка: Неподдерживаемая целевая система счисления!")
        return

    print(f"Результат: {result}")

convert_number()