def inp_int(text):
    print(text, end = " ")
    while True:
        i = input()
        if i.isdigit():
            return int(i)
        else:
            print("Пожалуйста введите целое число")

def inp_lang(text):
    print(text, end = " ")
    while True:
        i = input()
        if i == 'en' or i == 'ru':
            return i
        else:
            print("Пожалуйста введите en или ru")

def inp_nap(text):
    print(text, end = " ")
    while True:
        i = input()
        if i == 'sh' or i == 'des':
            return i
        else:
            print("Пожалуйста введите sh или des")

def caesar_cipher(text, nap, lang, step):
    result = ''
    if lang == 'en':
        if nap == 'sh':
            for el in text:
                if el.islower() and el.isalpha() and el.isspace() != True:
                    result += chr(ord('a') + (ord(el) - ord('a') + 26 + step) % 26)
                elif el.isupper() and el.isalpha() and el.isspace() != True:
                    result += chr(ord('A') + (ord(el) - ord('A') + 26 + step) % 26)
                elif el == " ":
                    result += " "
                else:
                    result += el
        else:
            for el in text:
                if el.islower() and el.isalpha() and el.isspace() != True:
                    result += chr(ord('a') + (ord(el) - ord('a') + 26 - step) % 26)
                elif el.isupper() and el.isalpha() and el.isspace() != True:
                    result += chr(ord('A') + (ord(el) - ord('A') + 26 - step) % 26)
                elif el == " ":
                    result += " "
                else:
                    result += el
    else:
        if nap == 'sh':
            for el in text:
                if el.islower() and el.isalpha() and el.isspace() != True:
                    result += chr(ord('а') + (ord(el) - ord('а') + 32 + step) % 32)
                elif el.isupper() and el.isalpha() and el.isspace() != True:
                    result += chr(ord('А') + (ord(el) - ord('А') + 32 + step) % 32)
                elif el == " ":
                    result += " "
                else:
                    result += el
        else:
            for el in text:
                if el.islower() and el.isalpha() and el.isspace() != True:
                    result += chr(ord('а') + (ord(el) - ord('а') + 32 - step) % 32)
                elif el.isupper() and el.isalpha() and el.isspace() != True:
                    result += chr(ord('А') + (ord(el) - ord('А') + 32 - step) % 32)
                elif el == " ":
                    result += " "
                else:
                    result += el
    return result

print("Добро пожаловать!")
nap = inp_nap("1. Выберите направление шифрования (введите sh или des):")
lang = inp_lang("2. Выберите язык алфавита (введите en или ru):")
step = inp_int("3. Введите шаг сдвига:")

text = input("4. Введите текст для шифрования/дешифрования: ")
result = caesar_cipher(text, nap, lang, step)
print("Результат шифрования:", result)