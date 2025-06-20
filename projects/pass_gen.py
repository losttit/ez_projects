import random

def inp_int(text):
    print(text, end = " ")
    while True:
        i = input()
        if i.isdigit():
            return int(i)
        else:
            print("Пожалуйста введите целое число")

def inp_y_n(text):
    print(text, end = " ")
    while True:
        i = input().lower()
        if i == "да" or i == "д" or i == "нет" or i == "н":
            return i
        else:
            print("Пожалуйста введите Да или Нет")

def generate_password(len, chars):
    password = ""
    for _ in range(len):
        password += random.choice(chars)
    return password


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
neodnoznachn = 'il1Lo0O?'
chars = ''
result = ''

print("Введите:")
num = inp_int("1. Количество паролей для генерации: ")
len = inp_int("2. Длину одного пароля: ")
dig = inp_y_n("3. Включать ли цифры 0123456789?")
ul = inp_y_n("4. Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?")
ll = inp_y_n("5. Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?")
sim = inp_y_n("6. Включать ли символы !#$%&*+-=?@^_?")
neod = inp_y_n("7. Исключать ли неоднозначные символы il1Lo0O?")

if dig == "да" or dig == "д":
    chars += digits
if ul == "да" or ul == "д":
    chars += uppercase_letters
if ll == "да" or ll == "д":
    chars += lowercase_letters
if sim == "да" or sim == "д":
    chars += punctuation
if neod == "да" or neod == "д":
    result = ''.join(char for char in chars if char not in neodnoznachn)

for _ in range(num):
    print(generate_password(len, result))
